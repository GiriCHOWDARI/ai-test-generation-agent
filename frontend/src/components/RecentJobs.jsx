export default function RecentJobs({ jobs }) {
  return (
    <div className="bg-white rounded-3xl shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">Recent Jobs</h2>
      <div className="space-y-4">
        {jobs.map((job, idx) => (
          <div key={idx} className="border rounded-2xl p-4 hover:shadow-md transition">
            <div className="flex items-center justify-between">
              <h3 className="font-bold text-gray-900">{job.project}</h3>
              <span className={`text-xs px-3 py-1 rounded-full ${
                job.status === 'Completed' ? 'bg-green-100 text-green-700' :
                job.status === 'Running' ? 'bg-yellow-100 text-yellow-700' :
                'bg-red-100 text-red-700'}`}>
                {job.status}
              </span>
            </div>
            <div className="mt-3 text-sm text-gray-600 space-y-1">
              <p>Model: {job.model}</p>
              <p>Generated Tests: {job.tests}</p>
              <p>Pass Rate: {job.passRate}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}