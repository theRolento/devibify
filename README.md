# Devibify

Devibify is a Codex skill for building and reviewing frontend UI without the usual vibe-coded tells: random gradients, decorative emoji, fake proof, inconsistent spacing, broken responsiveness, dead controls, missing loading states, and generic copy.

It turns UI work into a stricter product-design workflow: inspect the existing codebase, define a compact UI contract, reuse or establish a small design system, implement real states and interactions, then verify responsive behavior, accessibility basics, and technical polish before calling the work done.

## Install

Codex discovers local skills from the `skills` folder inside your Codex configuration directory. Install Devibify by placing the entire `devibify` folder inside that `skills` folder.

The installed folder should contain `SKILL.md` at its top level. Keep the `agents/openai.yaml` file inside the same `devibify` folder if you want Codex clients to show the skill with its display name, short description, and default prompt.

After installing, invoke it in Codex with:

```text
Use $devibify to redesign this page so it feels intentional, consistent, and production-ready.
```

## What It Includes

- A self-contained `SKILL.md` with the full no-vibe-coding workflow.
- A merged UI quality guide covering tokens, primitives, copy, layout, interaction states, accessibility, and verification.
- A vibe-coded website diagnostic report used as the main red-flag checklist.
- Optional skill UI metadata in `agents/openai.yaml`.

## Attribution

This skill was inspired by [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) by cyxzdev. Thanks to him for the original direction and idea.
