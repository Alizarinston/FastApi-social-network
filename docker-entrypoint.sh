#!/usr/bin/env bash

alembic revision --autogenerate -m "Added required tables" && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload