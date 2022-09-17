#!/bin/bash

alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8090 --workers 24 --reload --no-access-log