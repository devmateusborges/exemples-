/** @type {import('next').NextConfig} */
const path = require('path')
const nextConfig = {
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
    NEXT_PUBLIC_VERSION_BUILD: process.env.NEXT_PUBLIC_VERSION_BUILD,
    NEXT_PUBLIC_GA_MEASUREMENT_ID: process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID
  },
  reactStrictMode: true,
  experimental: {
    appDir: true,
  },
  sassOptions: {
    includePaths: [path.join(__dirname, 'styles')],
    prependData: `@import "~@styles/_variables.scss";`,
  },
  distDir: 'build',
}

module.exports = nextConfig


