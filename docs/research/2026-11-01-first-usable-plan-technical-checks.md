# Technical checks for the first usable implementation plan

Date: November 1, 2026. Read-only planning research; no application scaffold or dependency installation was performed.

## Runtime and database

The Mac runs Node v26.8.1. Importing `DatabaseSync` and `backup` from `node:sqlite` confirms both exports are functions on that exact runtime. Pin this runtime for the trial and isolate database access in the office persistence adapter. This avoids introducing a compiled SQLite addon solely for the first release. The current [Node SQLite documentation](https://nodejs.org/api/sqlite.html) describes the module as release-candidate, not a permanently stable API; tests and a runtime pin remain appropriate. Current online docs may describe a newer patch/API spelling than the installed runtime, so the local export check is the evidence for `DatabaseSync` at 26.8.1.

## Expo and workspace baseline

Read-only npm registry queries reported Expo 58.0.22 and blank TypeScript template 58.0.31. Expo's engine range admits Node 26. The template selects React 19.3.0, React Native 0.88.1, TypeScript ~6.0.3 and React types ~19.3.0. The actual Expo 58.0.22 package's `bundledNativeModules.json` selects React DOM 19.3.0, React Native Web ~0.21.4 and Metro runtime ~58.0.16. TypeScript latest is 7.0.2, but the plan should use the template-compatible 6.0.3 baseline rather than independently upgrading it.

[Expo monorepo documentation](https://docs.expo.dev/guides/monorepos/) supports npm workspaces with automatic configuration through `expo/metro-config`; no pre-SDK-52 resolver/watch-folder workaround is needed. [Expo Metro documentation](https://docs.expo.dev/guides/customizing-metro/) identifies the matching config import. These are proposed commands/configuration in the plan, not scaffold operations performed in this session.

Registry source: [Expo 58.0.22 metadata](https://registry.npmjs.org/expo/58.0.22) and [blank TypeScript template metadata](https://registry.npmjs.org/expo-template-blank-typescript/58.0.31). The Expo tarball was read in memory to inspect its compatibility matrix; it was not installed or extracted into the application workspace.

## Other observed package versions

| Package | Version observed |
| --- | --- |
| vite | 8.3.5 |
| vitest | 5.0.5 |
| dexie | 4.4.7 |
| decimal.js | 10.6.0 |
| zod | 4.6.7 |
| pdf-lib | 1.17.1 |
| fake-indexeddb | 6.2.7 |
| qrcode | 1.5.4 |
| @types/qrcode | 1.5.6 |
| jsqr | 1.4.0 |
| tsx | 4.23.15 |
| @types/node | 26.6.6 |
| @types/react | 19.3.0 |

`@vitejs/plugin-react` 6.1.2 reports Vite 8 plus compiler-related peer entries. The plan need not introduce a React Compiler pipeline for the trial; use only the transformations needed for the office UI. Final implementation records exact compatible dependencies in its lockfile.

## Validation boundary

Vitest fixtures/adapters and fake IndexedDB are useful automated checks; they do not prove Safari key persistence, browser storage eviction behavior, actual mail delivery or app-upgrade safety. The first usable release still requires the explicit iPhone/iPad installation, real version-upgrade, rotation, offline re-open and shared-calculation parity checks. Android hardware is unavailable and remains deferred. A browser automation framework is not a prerequisite for starting the trial.
