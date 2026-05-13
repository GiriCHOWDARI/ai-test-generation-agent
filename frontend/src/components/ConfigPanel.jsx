import { useState } from 'react';

export default function ConfigPanel() {
  const [validationMode, setValidationMode] = useState(
    localStorage.getItem('validationMode') || 'Strict'
  );
  const [retryAttempts, setRetryAttempts] = useState(
    localStorage.getItem('retryAttempts') || '3'
  );
  const [showToast, setShowToast] = useState(false);

  const handleSave = () => {
    localStorage.setItem('validationMode', validationMode);
    localStorage.setItem('retryAttempts', retryAttempts);
    setShowToast(true);
    setTimeout(() => setShowToast(false), 2500);
  };

  return (
    <div className="bg-white rounded-3xl shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">Configuration</h2>
      <div className="space-y-4">
        <div>
          <label className="text-sm font-medium text-gray-700">Validation Mode</label>
          <select
            value={validationMode}
            onChange={(e) => setValidationMode(e.target.value)}
            className="w-full mt-2 border rounded-2xl p-3"
          >
            <option>Strict</option>
            <option>Moderate</option>
            <option>Relaxed</option>
          </select>
        </div>
        <div>
          <label className="text-sm font-medium text-gray-700">Retry Attempts</label>
          <input
            type="number"
            value={retryAttempts}
            onChange={(e) => setRetryAttempts(e.target.value)}
            min="0"
            max="10"
            className="w-full mt-2 border rounded-2xl p-3"
          />
        </div>
        <button
          onClick={handleSave}
          className="w-full bg-black text-white py-3 rounded-2xl font-medium hover:scale-105 transition"
        >
          Save Configuration
        </button>
        {showToast && (
          <div className="text-sm text-green-600 text-center mt-2">
            ✅ Configuration saved!
          </div>
        )}
      </div>
    </div>
  );
}