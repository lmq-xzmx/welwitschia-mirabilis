/** @type {import('next').NextConfig} */
const isProd = process.env.NODE_ENV === 'production';

const nextConfig = {
    output: isProd ? 'export' : undefined,
    distDir: isProd ? '../static' : undefined,
    basePath: isProd ? '/static' : undefined,
    assetPrefix: isProd ? '/static' : undefined,
    eslint: {
        ignoreDuringBuilds: true,
    },
    typescript: {
        ignoreBuildErrors: true,
    },
    images: {
        unoptimized: true,
        remotePatterns: [
            {
                protocol: "https",
                hostname: "placehold.co",
            },
            {
                protocol: "http",
                hostname: "localhost",
                port: "17177",
            },
        ],
    },
};

export default nextConfig;
