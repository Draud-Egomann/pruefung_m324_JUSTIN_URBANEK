import globals from 'globals';

/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files:
      [
        '**/*.js',
      ],
    languageOptions:
      {
        ecmaVersion: 2021,
        sourceType:
          'module',
        globals:
          globals.browser,
      },
    rules:
      {
        'no-unused-vars':
          'error',
        'prefer-const':
          'error',
        eqeqeq:
          'error',
      },
  },
];
