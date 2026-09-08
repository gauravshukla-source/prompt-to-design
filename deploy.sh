#!/bin/bash

set -e

PROJECT_ID="architecture-diagram-500204"
REGION="us-central1"

SERVICE_NAME="enterprise-architecture-generator"

echo "======================================"
echo "Enterprise Architecture Generator"
echo "Deployment"
echo "======================================"

echo ""
echo "Project: $PROJECT_ID"
echo "Region: $REGION"
echo "Service: $SERVICE_NAME"

echo ""
echo "Running tests..."

python -m pytest -q

echo ""
echo "Tests passed."

echo ""
echo "Deploying to Cloud Run..."

gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --project "$PROJECT_ID" \
  --region "$REGION" \
  --allow-unauthenticated \
  --port 8080

echo ""
echo "Deployment complete."