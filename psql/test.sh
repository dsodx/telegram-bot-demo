#!/bin/bash
set -e

pg_isready -U $APP_USER -d $APP_DB
