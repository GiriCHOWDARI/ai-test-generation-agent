import { useState, useEffect, useRef } from 'react';
import { fetchStats, fetchPipeline, fetchJobs, fetchLogs, uploadProject, triggerGeneration } from './api';
import StatsCard from './components/StatsCard';
import Pipeline from './components/Pipeline';
import LogViewer from './components/LogViewer';
import RecentJobs from './components/RecentJobs';
import ConfigPanel from './components/ConfigPanel';

export default function AITestGenerationDashboard() {
  const fileInputRef = useRef(null);
  const [stats, setStats] = useState([
    { title: 'Generated Tests', value: '0' },
    { title: 'Runnable Tests', value: '0' },
    { title: 'Pass Rate', value: '0%' },
    { title: 'API Routes', value: '0' },
  ]);
  const [pipeline, setPipeline] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [logs, setLogs] = useState([]);

  const loadData = async () => {
    try {
      const statsData = await fetchStats();
      setStats([
        { title: 'Generated Tests', value: statsData.generated_tests.toString() },
        { title: 'Runnable Tests', value: statsData.runnable_tests.toString() },
        { title: 'Pass Rate', value: `${statsData.pass_rate}%` },
        { title: 'API Routes', value: statsData.api_routes.toString() },
      ]);
      setPipeline(await fetchPipeline());
      setJobs(await fetchJobs());
      setLogs(await fetchLogs());
    } catch (err) {
      console.error('Failed to load data:', err);
    }
  };

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  // Upload handling
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    try {
      const result = await uploadProject(file);
      alert(result.message || `Uploaded. ${result.routes_found} routes detected.`);
      await loadData();
    } catch (err) {
      console.error('Upload error:', err);
      alert('Upload failed.');
    }
    e.target.value = null;
  };

  const triggerUpload = () => {
    fileInputRef.current?.click();
  };

  // Generation handling
  const handleGenerate = async () => {
    try {
      const result = await triggerGeneration();
      if (result.status === 'error') {
        alert(result.message);
        return;
      }
      await loadData();
    } catch (err) {
      console.error('Generation error:', err);
      alert('Generation failed. Check the backend.');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="bg-white rounded-3xl shadow-lg p-6 flex flex-col md:flex-row md:items-center md:justify-between">
          <div>
            <h1 className="text-4xl font-bold text-gray-900">AI-Powered Test Generation Agent</h1>
            <p className="text-gray-600 mt-2 text-lg">
              Automated FastAPI pytest generation using AI agents, validation layers, and evaluation pipelines.
            </p>
          </div>

          <div className="mt-4 md:mt-0 flex gap-3">
            <button
              onClick={triggerUpload}
              className="border border-gray-300 px-6 py-3 rounded-2xl font-medium hover:bg-gray-100 transition"
            >
              Upload Project
            </button>
            <button
              onClick={handleGenerate}
              className="bg-black text-white px-6 py-3 rounded-2xl font-medium hover:scale-105 transition"
            >
              Generate Tests
            </button>
            <input
              ref={fileInputRef}
              type="file"
              accept=".py"
              onChange={handleFileChange}
              style={{ display: 'none' }}
            />
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
          {stats.map((item, idx) => (
            <StatsCard key={idx} title={item.title} value={item.value} />
          ))}
        </div>

        {/* Main Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 space-y-6">
            <Pipeline steps={pipeline} />
            <LogViewer logs={logs} />
          </div>
          <div className="space-y-6">
            <RecentJobs jobs={jobs} />
            <ConfigPanel />
          </div>
        </div>
      </div>
    </div>
  );
}