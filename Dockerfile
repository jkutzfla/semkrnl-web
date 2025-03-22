FROM node:22-alpine AS builder

WORKDIR /app
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


FROM python:3.12-slim
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY --from=builder /app/dist ./static
COPY backend/main.py ./
EXPOSE 5000
CMD ["python", "main.py"]