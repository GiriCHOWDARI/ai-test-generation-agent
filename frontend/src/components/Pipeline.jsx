export default function Pipeline({ steps }) {
  return (
    <div className="bg-white rounded-3xl shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Multi-Agent Pipeline</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {steps.map((step, idx) => (
          <div key={idx} className="p-5 rounded-2xl border bg-gray-50 hover:bg-black hover:text-white transition">
            <div className="text-sm font-semibold text-gray-500 hover:text-gray-300">Stage {idx + 1}</div>
            <div className="text-xl font-bold mt-2">{step}</div>
          </div>
        ))}
      </div>
    </div>
  );
}