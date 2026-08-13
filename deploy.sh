#!/bin/bash
# ============================================================
# deploy.sh — Build & deploy to Cloud Run via gcloud
# Run this in Google Cloud Shell or any machine with gcloud installed.
# ============================================================

set -e

PROJECT_ID="architecture-diagram-500204"
REGION="us-central1"
SERVICE_NAME="diagram-generator"

echo ">>> Setting project..."
gcloud config set project $PROJECT_ID

echo ">>> Enabling required APIs..."
gcloud services enable \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  containerregistry.googleapis.com \
  generativelanguage.googleapis.com \
  --project=$PROJECT_ID

# Grant the Cloud Run default service account the AI Platform User role
# so it can call the Generative Language API via ADC (no API key needed).
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"

echo ">>> Granting AI Platform User role to ${SA}..."
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SA}" \
  --role="roles/aiplatform.user" \
  --quiet

echo ">>> Building and deploying via Cloud Build..."
gcloud builds submit \
  --config cloudbuild.yaml \
  --project=$PROJECT_ID

echo ""
echo "Done! Your Cloud Run service URL:"
gcloud run services describe $SERVICE_NAME \
  --region=$REGION \
  --project=$PROJECT_ID \
  --format='value(status.url)'
