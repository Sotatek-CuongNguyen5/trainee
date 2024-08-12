#!/bin/bash
uvicorn app:app --host 0.0.0.0 --workers 3 --port 8000
