---
type: Analysis
id: TRACTION-MULTICLI-20261109
title: "Traction and project health comparison"
description: "Measured stars, age, contributor counts, commit activity, release cadence and download volume for Paseo, ZeroSub, Paseo Accounts, OpenMausBot and Orca."
status: candidate
date: 2026-11-09
tags: [orchestration, traction, project-health, cli-agents]
---

# Traction comparison

All figures pulled from the GitHub API and the npm registry on 2026-11-09. Contributor counts are unique non-anonymous logins across all pages; activity windows come from `repos/{repo}/stats/contributors`, which reports 52 weekly buckets per contributor.

## Headline table

| | **Paseo** | **ZeroSub** | Paseo Accounts | **OpenMausBot** | Orca |
|---|---:|---:|---:|---:|---:|
| Repository | `getpaseo/paseo` | `kapybara-org/zerosub` | `jgreys/paseo-accounts` | `milind-soni/OpenMausBot` | `stablyai/orca` |
| **Stars** | **23,635** | 22 | **1** | **19,452** | 120,165 |
| Forks | 2,897 | 23 | 1 | 2,673 | 7,616 |
| Watchers | 56 | 0 | 0 | 46 | 161 |
| Open issues | 1,889 | 9 | 0 | 942 | 8,287 |
| **Created** | 2025-10-13 | 2026-09-23 | 2026-10-20 | 2026-08-11 | 2026-03-17 |
| **Age** | **~13 months** (392 d) | **47 days** | **20 days** | **~3 months** (90 d) | ~8 months |
| Last push | 2026-11-09 | 2026-11-09 | **2026-11-01** | 2026-11-09 | 2026-11-09 |
| **Total contributors** | **226** | **6** | **1** | **210** | — |
| **Active, last 4 weeks** | **39** | **6-9** | **1** | **58** | — |
| Active, last 12 weeks | 61 | 9 | 1 | 95 | — |
| Commits, last 4 weeks | 583 | 55 | ~9 lifetime | **4,253** | — |
| Commits, last 52 weeks | 6,841 | 73 | ~9 | 10,193 | — |
| Releases published | 220 | 7+ tags | 0 | 107 | — |
| Latest release | v0.15.3, 2026-11-06 | v1.5.1 | none | v0.1.150, 2026-11-09 | — |
| Release cadence | ~17/month | ~5/month | — | **~36/month** | — |
| **Release downloads, latest** | **613,006** | n/a (plugin) | n/a | 52,791 | — |
| Release downloads, last 10 | **3,085,903** | n/a | n/a | 392,695 | — |
| **npm package** | n/a (desktop app) | `@kapybara/zerosub` | **not published (404)** | `openmausbot` | — |
| npm downloads, last month | — | **3,596** | 0 | **16,453** | — |
| npm downloads, last week | — | 1,189 | 0 | — | — |
| Licence | Apache-2.0 (own code) | MIT | MIT | Apache-2.0 | MIT |
| Language | TypeScript | TypeScript | TypeScript | TypeScript | TypeScript |
| Repo size | 197 MB | <1 MB | 1 MB | 479 MB | 2,547 MB |

Dashes mark figures not pulled for Orca, which is the fallback option rather than a finalist.

## Reading the numbers

**Paseo and OpenMausBot are both large, serious projects. ZeroSub is not, and does not need to be.**

- **Paseo** is the older and more distributed of the two majors: 13 months old, 226 contributors, 39 active in the last month, and **3.09 million downloads across its last 10 releases alone**. Its newest release took 613,006 downloads in three days. On raw distribution it is the most-used piece of software in this comparison by a wide margin.
- **OpenMausBot** is younger but faster-moving: 19,452 stars in **90 days** is a star velocity of roughly 6,500/month against Paseo's ~1,800/month, and 4,253 commits in the last four weeks is **7.3x** Paseo's 583. It has 210 contributors with 58 active this month — more active contributors than Paseo. It releases roughly every 20 hours.
- **ZeroSub is a 47-day-old plugin with 6 contributors and 49 commits.** It has 22 stars. Judged as a project in its own right that is small. Judged as what it actually is — a focused plugin on top of a 23,635-star host — the signals that matter are different and they are good: all 6 contributors committed in the last four weeks, 55 of its 73 lifetime commits landed in that window, it has shipped 7 tagged releases, and its npm downloads are **3,596 last month and 1,189 in the last week alone**, which annualises to a growing run-rate rather than a dormant one.

**Paseo Accounts is the one that fails on traction, decisively.** One star, one contributor, nine commits, twenty days old, eight days since the last push, zero releases, zero open issues, and **it is not published on npm at all** — `@jgreys/paseo-accounts` returns 404. Against ZeroSub's 6 active contributors and 3,596 monthly downloads it is not a serious comparator, which closes the question the source research document left open.

## What this does and does not change

It **confirms** the maintenance-health scores in `RANKING-weighted-model.md` (V11, weight 4) rather than changing them: Paseo + ZeroSub at 70, OpenMausBot at 85. Both sit where the measurements put them, and neither moves enough to shift a composite that V11 contributes at most 4 points to.

It **hardens** two conclusions already reached:

1. ZeroSub over Paseo Accounts is now beyond argument — the derived plugin is not merely thinner, it is unpublished.
2. Neither finalist is a project-health risk. The risk that decides this selection is not whether these projects survive; it is whether same-provider rotation works on Windows with Codex, which only Phase 2 can answer.

## The honest caveat on the comparison

Stars, downloads and commit counts measure adoption and momentum. They do **not** measure whether the specific capability you need works on your specific host. Paseo's 3.09 million downloads say nothing about whether its account plugin rotates a Codex login on Windows 11 — its own `TESTING.md` still puts that under "Only covered by automated tests". A popular project with an unproven feature and an unpopular project with a proven one would rank the same way on this page and oppositely on the one that matters.
