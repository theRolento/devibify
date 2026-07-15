# Devibify

Devibify is a Codex skill for building and reviewing frontend UI as a coherent product system rather than a stock, vibe-coded composition.

It guides UI work through a checkable workflow: inspect the product, define a compact UI contract, reuse or establish a small visual system, implement real states and interactions, run a comprehensive audit, and verify the result.

## Install

Codex discovers local skills from the `skills` folder inside your Codex configuration directory. Install Devibify by placing the entire `devibify` folder inside that `skills` folder.

The installed folder should contain `SKILL.md` at its top level. Keep the `agents/openai.yaml` file inside the same `devibify` folder if you want Codex clients to show the skill with its display name, short description, and default prompt.

After installing, invoke it in Codex with:

```text
Use $devibify to review and refine this UI so it avoids vibe-coded tells and feels intentional, consistent, and production-ready.
```

## What It Includes

- A concise `SKILL.md` with the core devibify workflow and explicit completion criteria.
- A progressively disclosed UI audit covering composition, visual systems, content integrity, components, responsive behavior, accessibility, and page completeness.
- Optional skill UI metadata in `agents/openai.yaml`.

## Attribution

This skill was inspired by [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) by cyxzdev. Thanks to him for the original direction and idea.
