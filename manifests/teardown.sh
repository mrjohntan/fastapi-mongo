#!/bin/sh
kubectl delete -f mongo-service.yaml
kubectl delete -f mongo-deployment.yaml
kubectl delete -f mongo-secrets.yaml
kubectl delete -f mongo-pvc.yaml
kubectl delete -f mongo-pv.yaml



