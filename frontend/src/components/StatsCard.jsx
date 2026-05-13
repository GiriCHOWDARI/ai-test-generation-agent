export default function StatsCard({ title, value }) {
  return (
    <div className="bg-white rounded-3xl shadow-md p-6 hover:shadow-xl transition">
      <p className="text-gray-500 text-sm">{title}</p>
      <h2 className="text-4xl font-bold mt-2 text-gray-900">{value}</h2>
    </div>
  );
}