/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
const colors = require('tailwindcss/colors')

module.exports = {

    darkMode: 'media',
    theme: {
        extend: {
            colors: {
            'dark-main': '#18191A',
            'dark-second': '#242526',
            'dark-third': '#3A3B3C',
            'dark-txt': '#B8BBBF',
            sky: colors.sky,
            teal: colors.teal,
            rose: colors.rose,
                },
            },
        },
    content: [
        



        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

    ],

    variants: {
        extend: {
            display: ['group-hover'],
            transform: ['group-hover'],
            scale: ['group-hover'],
            textOpacity: ['dark'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        /*
                AGREGADOOOO || 
                    abajo   V
         */
        require('tailwind-scrollbar-hide')
    ],
}
