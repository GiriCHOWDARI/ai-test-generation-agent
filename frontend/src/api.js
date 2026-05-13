const BASE_URL = 'http://localhost:8000/api';

export async function fetchStats() {
  const res = await fetch(`${BASE_URL}/stats`);
  return res.json();
}

export async function fetchPipeline() {
  const res = await fetch(`${BASE_URL}/pipeline`);
  return res.json();
}

export async function fetchJobs() {
  const res = await fetch(`${BASE_URL}/jobs`);
  return res.json();
}

export async function fetchLogs() {
  const res = await fetch(`${BASE_URL}/logs`);
  return res.json();
}

export async function uploadProject(file) {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${BASE_URL}/upload`, {
    method: 'POST',
    body: formData,
  });
  return res.json();
}

export async function triggerGeneration() {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: 'POST',
  });
  return res.json();
}