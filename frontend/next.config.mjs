const API = process.env.BACKEND_URL || "http://localhost:8000";

const nextConfig = {
  async rewrites() {
    return [{ source: "/api/:path*", destination: `${API}/api/:path*` }];
  },
};

export default nextConfig;
