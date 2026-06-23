# ============================================================
# download-promptquorum-pe.ps1
# Downloads PromptQuorum Prompt Engineering articles as Markdown
# Uses r.jina.ai - no extra tools needed beyond PowerShell
# Run: Set-ExecutionPolicy Bypass -Scope Process
#      .\download-promptquorum-pe.ps1
# ============================================================

$base = "C:\GitDev\apexai-os-meta\source-knowledge\old_openclaw-KB&Agents\special_ops__prompts_workflows\NewResearchBlueprints\Quantum-PE"
$jina = "https://r.jina.ai"

# Create subfolders
New-Item -ItemType Directory -Force -Path "$base\evaluation" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\frameworks" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\fundamentals" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\local-llms" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\team-governance" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\techniques" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\tools" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\use-cases" | Out-Null

Write-Host "Downloading 69 articles from PromptQuorum..."
Write-Host "Output: $base"
Write-Host ""

Write-Host "  [1/69] fundamentals/what-is-prompt-engineering"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/what-is-prompt-engineering") -OutFile "$base\fundamentals\what-is-prompt-engineering.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] what-is-prompt-engineering" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [2/69] fundamentals/how-to-optimize-prompts"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/how-to-optimize-prompts") -OutFile "$base\fundamentals\how-to-optimize-prompts.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] how-to-optimize-prompts" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [3/69] fundamentals/history-of-prompt-engineering"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/history-of-prompt-engineering") -OutFile "$base\fundamentals\history-of-prompt-engineering.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] history-of-prompt-engineering" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [4/69] fundamentals/5-building-blocks-every-prompt-needs"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/5-building-blocks-every-prompt-needs") -OutFile "$base\fundamentals\5-building-blocks-every-prompt-needs.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] 5-building-blocks-every-prompt-needs" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [5/69] fundamentals/ai-hallucinations"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/ai-hallucinations") -OutFile "$base\fundamentals\ai-hallucinations.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ai-hallucinations" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [6/69] fundamentals/ai-limitations"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/ai-limitations") -OutFile "$base\fundamentals\ai-limitations.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ai-limitations" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [7/69] fundamentals/faster-ai-answers"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/faster-ai-answers") -OutFile "$base\fundamentals\faster-ai-answers.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] faster-ai-answers" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [8/69] fundamentals/temperature-and-top-p"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/temperature-and-top-p") -OutFile "$base\fundamentals\temperature-and-top-p.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] temperature-and-top-p" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [9/69] fundamentals/context-windows-explained"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/context-windows-explained") -OutFile "$base\fundamentals\context-windows-explained.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] context-windows-explained" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [10/69] fundamentals/beyond-text-prompting-with-images"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/beyond-text-prompting-with-images") -OutFile "$base\fundamentals\beyond-text-prompting-with-images.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] beyond-text-prompting-with-images" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [11/69] fundamentals/tokens-costs-limits"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/tokens-costs-limits") -OutFile "$base\fundamentals\tokens-costs-limits.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] tokens-costs-limits" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [12/69] fundamentals/system-prompt-vs-user-prompt"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/system-prompt-vs-user-prompt") -OutFile "$base\fundamentals\system-prompt-vs-user-prompt.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] system-prompt-vs-user-prompt" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [13/69] fundamentals/gpt-claude-or-gemini"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/gpt-claude-or-gemini") -OutFile "$base\fundamentals\gpt-claude-or-gemini.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] gpt-claude-or-gemini" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [14/69] fundamentals/how-llms-actually-work"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/how-llms-actually-work") -OutFile "$base\fundamentals\how-llms-actually-work.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] how-llms-actually-work" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [15/69] fundamentals/open-source-vs-proprietary-llms"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/open-source-vs-proprietary-llms") -OutFile "$base\fundamentals\open-source-vs-proprietary-llms.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] open-source-vs-proprietary-llms" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [16/69] fundamentals/prompt-engineering-glossary"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary") -OutFile "$base\fundamentals\prompt-engineering-glossary.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-glossary" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [17/69] frameworks/which-prompt-framework-should-you-use"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/which-prompt-framework-should-you-use") -OutFile "$base\frameworks\which-prompt-framework-should-you-use.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] which-prompt-framework-should-you-use" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [18/69] frameworks/single-step-prompt-method"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/single-step-prompt-method") -OutFile "$base\frameworks\single-step-prompt-method.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] single-step-prompt-method" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [19/69] frameworks/ape-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/ape-framework") -OutFile "$base\frameworks\ape-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ape-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [20/69] frameworks/craft-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/craft-framework") -OutFile "$base\frameworks\craft-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] craft-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [21/69] frameworks/co-star-prompt-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/co-star-prompt-framework") -OutFile "$base\frameworks\co-star-prompt-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] co-star-prompt-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [22/69] frameworks/specs-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/specs-framework") -OutFile "$base\frameworks\specs-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] specs-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [23/69] frameworks/risen-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/risen-framework") -OutFile "$base\frameworks\risen-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] risen-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [24/69] frameworks/trace-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/trace-framework") -OutFile "$base\frameworks\trace-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] trace-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [25/69] frameworks/googles-prompting-guide"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/googles-prompting-guide") -OutFile "$base\frameworks\googles-prompting-guide.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] googles-prompting-guide" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [26/69] frameworks/rtf-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/rtf-framework") -OutFile "$base\frameworks\rtf-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] rtf-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [27/69] frameworks/build-your-own-prompt-framework"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework") -OutFile "$base\frameworks\build-your-own-prompt-framework.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] build-your-own-prompt-framework" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [28/69] techniques/chain-of-thought-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting") -OutFile "$base\techniques\chain-of-thought-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] chain-of-thought-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [29/69] techniques/few-shot-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/few-shot-prompting") -OutFile "$base\techniques\few-shot-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] few-shot-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [30/69] techniques/zero-shot-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/zero-shot-prompting") -OutFile "$base\techniques\zero-shot-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] zero-shot-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [31/69] techniques/rag-retrieval-augmented-generation"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/rag-retrieval-augmented-generation") -OutFile "$base\techniques\rag-retrieval-augmented-generation.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] rag-retrieval-augmented-generation" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [32/69] techniques/self-consistency-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/self-consistency-prompting") -OutFile "$base\techniques\self-consistency-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] self-consistency-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [33/69] techniques/role-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/role-prompting") -OutFile "$base\techniques\role-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] role-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [34/69] techniques/tree-of-thought-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/tree-of-thought-prompting") -OutFile "$base\techniques\tree-of-thought-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] tree-of-thought-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [35/69] techniques/meta-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/meta-prompting") -OutFile "$base\techniques\meta-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] meta-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [36/69] techniques/structured-output-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/structured-output-prompting") -OutFile "$base\techniques\structured-output-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] structured-output-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [37/69] techniques/negative-prompting"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/negative-prompting") -OutFile "$base\techniques\negative-prompting.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] negative-prompting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [38/69] evaluation/how-to-evaluate-prompt-quality"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/how-to-evaluate-prompt-quality") -OutFile "$base\evaluation\how-to-evaluate-prompt-quality.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] how-to-evaluate-prompt-quality" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [39/69] evaluation/prompt-regression-testing"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-regression-testing") -OutFile "$base\evaluation\prompt-regression-testing.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-regression-testing" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [40/69] evaluation/cross-model-testing"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/cross-model-testing") -OutFile "$base\evaluation\cross-model-testing.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] cross-model-testing" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [41/69] evaluation/prompt-evaluation-metrics"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-evaluation-metrics") -OutFile "$base\evaluation\prompt-evaluation-metrics.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-evaluation-metrics" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [42/69] evaluation/llm-as-judge"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/llm-as-judge") -OutFile "$base\evaluation\llm-as-judge.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] llm-as-judge" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [43/69] evaluation/prompt-reliability"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-reliability") -OutFile "$base\evaluation\prompt-reliability.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-reliability" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [44/69] evaluation/hallucination-detection"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/hallucination-detection") -OutFile "$base\evaluation\hallucination-detection.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] hallucination-detection" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [45/69] team-governance/prompt-version-control"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-version-control") -OutFile "$base\team-governance\prompt-version-control.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-version-control" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [46/69] team-governance/prompt-engineering-setup-small-teams"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-setup-small-teams") -OutFile "$base\team-governance\prompt-engineering-setup-small-teams.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-setup-small-teams" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [47/69] team-governance/build-a-prompt-library"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/build-a-prompt-library") -OutFile "$base\team-governance\build-a-prompt-library.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] build-a-prompt-library" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [48/69] team-governance/prompt-ci-cd"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-ci-cd") -OutFile "$base\team-governance\prompt-ci-cd.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-ci-cd" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [49/69] team-governance/prompt-governance"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-governance") -OutFile "$base\team-governance\prompt-governance.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-governance" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [50/69] team-governance/prompt-review-gates"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-review-gates") -OutFile "$base\team-governance\prompt-review-gates.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-review-gates" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [51/69] tools/best-prompt-engineering-tools-2026"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/best-prompt-engineering-tools-2026") -OutFile "$base\tools\best-prompt-engineering-tools-2026.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] best-prompt-engineering-tools-2026" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [52/69] tools/best-prompt-management-platforms"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/best-prompt-management-platforms") -OutFile "$base\tools\best-prompt-management-platforms.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] best-prompt-management-platforms" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [53/69] tools/promptlayer-vs-mirascope-vs-promptperfect"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/promptlayer-vs-mirascope-vs-promptperfect") -OutFile "$base\tools\promptlayer-vs-mirascope-vs-promptperfect.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] promptlayer-vs-mirascope-vs-promptperfect" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [54/69] tools/braintrust-review"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/braintrust-review") -OutFile "$base\tools\braintrust-review.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] braintrust-review" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [55/69] tools/promptfoo-review"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/promptfoo-review") -OutFile "$base\tools\promptfoo-review.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] promptfoo-review" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [56/69] tools/prompthub-review"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompthub-review") -OutFile "$base\tools\prompthub-review.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompthub-review" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [57/69] tools/cursor-for-prompt-engineering"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/cursor-for-prompt-engineering") -OutFile "$base\tools\cursor-for-prompt-engineering.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] cursor-for-prompt-engineering" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [58/69] tools/vellum-review"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/vellum-review") -OutFile "$base\tools\vellum-review.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] vellum-review" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [59/69] local-llms/how-to-run-local-llms"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/how-to-run-local-llms") -OutFile "$base\local-llms\how-to-run-local-llms.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] how-to-run-local-llms" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [60/69] local-llms/ollama-guide"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/ollama-guide") -OutFile "$base\local-llms\ollama-guide.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ollama-guide" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [61/69] local-llms/lm-studio-guide"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/lm-studio-guide") -OutFile "$base\local-llms\lm-studio-guide.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] lm-studio-guide" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [62/69] local-llms/best-local-llm-models"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/best-local-llm-models") -OutFile "$base\local-llms\best-local-llm-models.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] best-local-llm-models" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [63/69] local-llms/hardware-for-local-llms"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/hardware-for-local-llms") -OutFile "$base\local-llms\hardware-for-local-llms.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] hardware-for-local-llms" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [64/69] use-cases/prompt-engineering-for-coding"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-for-coding") -OutFile "$base\use-cases\prompt-engineering-for-coding.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-for-coding" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [65/69] use-cases/prompt-engineering-for-research"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-for-research") -OutFile "$base\use-cases\prompt-engineering-for-research.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-for-research" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [66/69] use-cases/prompt-engineering-for-writing"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-for-writing") -OutFile "$base\use-cases\prompt-engineering-for-writing.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-for-writing" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [67/69] use-cases/prompt-engineering-for-data-analysis"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-for-data-analysis") -OutFile "$base\use-cases\prompt-engineering-for-data-analysis.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-for-data-analysis" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [68/69] use-cases/ai-code-review"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/ai-code-review") -OutFile "$base\use-cases\ai-code-review.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ai-code-review" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [69/69] use-cases/prompt-engineering-for-customer-support"
try {
  Invoke-WebRequest -Uri ("$jina/https://www.promptquorum.com/prompt-engineering/prompt-engineering-for-customer-support") -OutFile "$base\use-cases\prompt-engineering-for-customer-support.md" -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] prompt-engineering-for-customer-support" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

# Save index page
Write-Host "  [index] Saving index page..."
Invoke-WebRequest -Uri ($jina + "/https://www.promptquorum.com/prompt-engineering") -OutFile "$base\INDEX.md" -UseBasicParsing

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
$count = (Get-ChildItem -Path $base -Recurse -Filter "*.md").Count
Write-Host "$count files saved to $base" -ForegroundColor Cyan
explorer.exe $base