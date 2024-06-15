# Personalized LLM Research Assistent (个性化大语言模型领域研究助理)

随着大语言模型(LLMs)
在自然语言处理领域取得显著进展,其在人机交互方面展现出巨大潜力。然而,当前LLMs主要对齐整体人类偏好,难以充分满足用户的个性化需求。鉴于人类价值观和偏好的多样性,以及语用在人际交互中的重要性,我们认为LLMs的发展需要从对齐群体偏好转向个性化。个性化大语言模型(
Personalized LLM)被认为是LLMs发展历程中的下一个重要步骤,但目前尚未在大规模应用中得到充分实现[1]
。作为一个前沿研究领域,学者们迫切需要一个可靠的工具来回答与该领域相关的专业问题。
我们的目标是开发一个定制化的问答机器人,专注于为学者提供个性化大语言模型领域的专业知识和有价值的参考资料。
该机器人将具备以下特点:

1. 专业性:深入了解个性化大语言模型领域的最新进展,提供权威、可靠的信息。
2. 交互性:通过自然语言交互,营造友好、高效的问答体验,鼓励学者深入探讨。
3. 可扩展性:随着研究的深入,不断更新知识库,确保信息与时俱进。

我们相信,这样一个专注于个性化大语言模型领域的定制化问答机器人,将为学者们提供强有力的支持,促进该领域的研究和创新。

[1] Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models
with personalised feedback HR Kirk, B Vidgen, P Röttger, SA Hale - arXiv preprint arXiv:2303.05453, 2023

## 技术路线

具体来说,我们将采用以下技术框架:

![Personalized LLM Research Assistent](./asset/framework.png)

如上图所示,我们的系统由以下几个模块组成:

- Dataset: 个性化大语言模型领域的专业知识和有价值的参考资料。
- Model: 个性化大语言模型,用于回答用户提出的问题, 包括 InternLM2, Llamm3, DeepseekV2等。
- Method: 探索多种方法, 包括 RAG, 增量预训练, SFT, 偏好学习等, 帮助模型获得领域专业知识, 成为个性化大模型领域研究助理.
- Application: 模型评估, 推理优化, 模型部署等.

### 1. Dataset

我们的数据集是从个性化大语言模型领域的专业知识和有价值的参考资料中提取的, 通过专业人员的筛选, 整理, 生成的。


### 2. Model


我们将采用多种大语言模型, 包括 InternLM2, Llamm3, DeepseekV2等, 用于回答用户提出的问题。


### 3. Method

.... 

### 4. Application


.... 


## 常见问题 QA

Q1. 为什么要开发这个机器人?

A1. 个性化大语言模型领域是一个前沿研究领域,学者们迫切需要一个可靠的工具来回答与该领域相关的专业问题。更加具体的来说,
是我们正在进行一个个性化大语言模型的研究项目, 所以需要一个该领域的研究助理, 帮助整理文献, 写作论文, 启发思考等.

Q2. 直接使用茴香豆做 RAG 不就够了吗? 为什么还在考虑微调?

A2. RAG 技术很好, 但是模型没有深入理解个性化大语言模型领域的专业知识和有价值的参考资料, 所以需要微调. 考虑最强大的
RAG 技术, 我们制作的 GPT Agent for Personalized LLM Research, 效果完全达不到我们的预期. 所以我们的目的是希望大模型能真正的掌握这个领域的专业知识,
这样或许能成为我们更好的科研助理。

Q3. 微调数据集如何获得?

A3. 我们的数据集是从个性化大语言模型领域的专业知识和有价值的参考资料中提取的, 通过专业人员的筛选, 整理, 生成的.


Q4. 和书生·浦语大模型实战营什么关系?

A4. 书生·浦语大模型实战营是学习大模型全链路开发的系统化课程, 个性化大语言研究助理项目的开发依赖于这些知识的掌握.







---

**本项目是上海人工智能实验室的实战营项目，项目的目标的另外一个目的深入学习大模型全链路开发. **

# 书生·浦语大模型实战营

![](./asset/camp.png)

为了推动大模型在更多行业落地开花，让开发者们更高效的学习大模型的开发与应用，上海人工智能实验室重磅推出书生·浦语大模型实战营，为广大开发者搭建大模型学习和实践开发的平台，两周时间带你玩转大模型微调、部署与评测全链路。

实战营春季第4补增场火热报名中，欢迎填写[表单](https://www.wjx.top/vm/Yzzz2mi.aspx?udsid=876275)报名！  
报名成功后加入群聊，私聊助教或者浦语小助手获取免费 A100 算力支持！！！

## 😊 你将获得

👨‍🏫 实力讲师：来自前沿科研机构、一线大厂和 Github 热门开源项目的讲师手把手教学  
💻 算力支持：算力资源免费提供，助力无忧训练大模型  
💬 专属社群：助教、讲师全程陪伴，提供录播回放、线上答疑及实战作业辅导  
📜 官方认证：优秀学员将获得荣誉证书，优秀项目有机会被官方收录，获得更多展示

## 📅 课程安排

| 课程时间  | 课程内容                            | 讲师                                                | 资料                                                                                             |
|:------|:--------------------------------|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| 第 1 节 | 书生·浦语大模型全链路开源体系                 | 陈恺 </br>上海人工智能实验室青年科学家                            | [视频](https://www.bilibili.com/video/BV1Rc411b7ns/)                                             |
| 第 2 节 | 轻松玩转书生·浦语大模型趣味 Demo             | 宋志学</br>d2l-ai-solutions-manual 开源项目负责人           | [文档](./helloworld/hello_world.md)、[视频](https://www.bilibili.com/video/BV1Ci4y1z72H)            |
| 第 3 节 | 基于 InternLM 和 LangChain 搭建你的知识库 | 邹雨衡</br>prompt-engineering-for-developers 开源项目负责人 | [文档](./langchain/readme.md)、[视频](https://www.bilibili.com/video/BV1sT4y1p71V/)                 |
| 第 4 节 | XTuner 大模型单卡低成本微调实战             | 汪周谦</br>XTuner 社区贡献者                              | [文档](./xtuner/README.md)、[视频](https://www.bilibili.com/video/BV1yK4y1B75J)                     |
| 第 5 节 | LMDeploy 大模型量化部署实践              | 长琴</br>HuggingLLM开源项目负责人                          | [文档](./lmdeploy/lmdeploy.md)、[视频](https://www.bilibili.com/video/BV1iW4y1A77P)                 |
| 第 6 节 | OpenCompass 大模型评测               | 曹茂松</br>OpenCompass 核心开发者                         | [文档](./opencompass/opencompass_tutorial.md)、[视频](https://www.bilibili.com/video/BV1Gg4y1U7uc/) |
| 第 7 节 | 彩蛋环节                            | 神秘嘉宾                                              | 文档、视频                                                                                          |

## 📝 作业

助教老师将在社群中公布每节课的作业及提交方式

## 🖥️ 算力平台

https://studio.intern-ai.org.cn/

问卷中的核销码为邀请码，如额外需要充值算力或者其他任何疑问请联系浦语小助手(微信号搜索：InternLM)