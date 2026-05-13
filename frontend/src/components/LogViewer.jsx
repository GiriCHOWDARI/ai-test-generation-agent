export default function LogViewer({ logs }) {
  return (
    <div className="bg-white rounded-3xl shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">Generation Logs</h2>
      <div className="bg-black text-green-400 rounded-2xl p-5 font-mono text-sm h-72 overflow-y-auto">
        {logs.map((line, i) => <p key={i}>{line}</p>)}
      </div>
    </div>
  );
}