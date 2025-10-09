/** @type {import('prettier').Config & import('prettier-plugin-tailwindcss').PluginOptions} */
export default {
  plugins: ["prettier-plugin-tailwindcss"],
  "tailwindStylesheet": "./static/src/styles.css",
  "tailwindPreserveWhitespace": true,
  "tailwindConfig": "tailwind.config.js"
}