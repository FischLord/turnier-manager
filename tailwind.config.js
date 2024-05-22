module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/js/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1E1E2E',
        secondary: '#252537',
        accent: '#3B82F6',
        text: '#E5E5E5',
        formbg: '#2A2A3C',
        formborder: '#3B3B51',
        hover: '#4B4B6B',
      },
      borderRadius: {
        'lg': '0.5rem',
      },
      transitionTimingFunction: {
        'smooth': 'ease-in-out',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
