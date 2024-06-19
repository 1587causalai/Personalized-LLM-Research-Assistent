import json

data = {
    "questions_and_answers": [
        {
            "question": "为什么评估基准在研究社区中如此重要？",
            "answer": "评估基准是研究社区的激励因素，与突破性成果密切相关。突破性成果通常与评估基准上的显著性能提升有关。"
        },
        {
            "question": "一个成功的评估基准的标准是什么？",
            "answer": "成功的评估基准被突破性论文使用，并且在研究社区内被信任。"
        },
        {
            "question": "过去五年中有哪些成功的评估基准？",
            "answer": "成功的评估基准包括GLUE/SuperGLUE、MMLU、GSM8K、MATH和HumanEval，以及其他如HellaSwag和SQuAD。"
        },
        {
            "question": "成功的评估基准有哪些共同特征？",
            "answer": "成功的评估基准通常伴随着重要论文的推广和胜利。例如，GLUE与BERT，MMLU与Gopher、Chinchilla、Flan-PaLM，GSM8K与思维链突破，MATH与Minerva，HumanEval与Codex等。"
        },
        {
            "question": "Jason Wei创建的评估基准是什么？这些基准如何使用？",
            "answer": "Jason Wei创建了MGSM和BBH。MGSM用于OpenAI的简单评估、Claude、Gemini；BBH用于Claude、Gemini、Llama。他认为这些评估基准还不错，但不是最好的。"
        }
    ]
}

with open("questions_and_answers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)