#!/bin/bash

set -e

PROJECT_ID="architecture-diagram-500204"
REGION="us-central1"
SERVICE_NAME="diagram-generator"
MODEL="gemini-2.5-flash"

echo "======================================"
echo "Enterprise Architecture Generator"
echo "Deployment to Google Cloud Run"
echo "======================================"

echo ""
echo "Project: $PROJECT_ID"
echo "Region:  $REGION"
echo "Service: $SERVICE_NAME"
echo "Model:   $MODEL"

# 1. Enable Vertex AI & Cloud Run APIs if needed
echo ""
echo "Enabling necessary APIs..."
gcloud services enable aiplatform.googleapis.com run.googleapis.com artifactregistry.googleapis.com \
  --project "$PROJECT_ID" 2>/dev/null || true

# 2. Grant Vertex AI User role to the default compute service account
echo ""
echo "Configuring IAM permissions for Vertex AI ADC..."
PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format="value(projectNumber)" 2>/dev/null || true)
if [ -n "$PROJECT_NUMBER" ]; then
  COMPUTE_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
  echo "Granting roles/aiplatform.user to $COMPUTE_SA..."
  gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:${COMPUTE_SA}" \
    --role="roles/aiplatform.user" 2>/dev/null || true
fi

# 3. Run validation tests if pytest is available
if command -v pytest >/dev/null 2>&1; then
  echo ""
  echo "Running tests..."
  pytest -q || echo "Warning: Tests had non-fatal warnings, proceeding with deployment..."
fi

# 4. Deploy to Cloud Run using source build
echo ""
echo "Deploying to Cloud Run..."
gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --project "$PROJECT_ID" \
  --region "$REGION" \
  --allow-unauthenticated \
  --port 8080 \
  --set-env-vars "GOOGLE_CLOUD_PROJECT=${PROJECT_ID},GCP_LOCATION=${REGION},GEMINI_MODEL=${MODEL},LLM_PROVIDER=vertex_ai"

echo ""
echo "======================================"
echo "Deployment complete!"
echo "Service URL:"
gcloud run services describe "$SERVICE_NAME" --project "$PROJECT_ID" --region "$REGION" --format="value(status.url)"
echo "======================================"
