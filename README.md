# Arbeitszeugnis.ai

Decode complex german job references, powered by Gemini Pro.

Just upload your job reference and see your real ratings.

## Demo

## Motivation

German job references (german: _arbeitszeugnis_) are handed out to an employee after leaving a company. In addition to a description of the company, the department and the activities during the employment relationship, the employee himself is also evaluated. There are various criteria such as the quality of work, resilience, behavior towards employees, management style, working methods and so on.

A big problem with job references is that they are written in a benevolent way (as a legal safeguard), which is why it is sometimes not as easy to see how they are valued. A rating can be very poor and still be formulated positively, which makes it difficult to decipher.

This is why I wanted to build a tool, which helps in decoding the job references and see which ratings you really got.

## Limitations

1. I built something similar in October 2022 with BERT for decoding the job references and collected a good amount of data back then. But after formatting my machine, I lost all the data :') This is the main reason why this tool may not work perfectly.

2. Moreover I used the Gemini Pro API from Google, because it's for free (right now). Therefore it is possible that you can not use it from everywhere (see [eligible regions](https://ai.google.dev/available_regions)). While developing this tool, I usually had to use a VPN and set my location to USA, because the API isn't available in Germany.

3. Since you can't finetune Gemini Pro (right now), I inserted some examples for job reference sentences and their corresponding rating and category into the prompt. This results in a prompt with ~6k tokens (without the job reference itself). Of course, you and I don't mind about it since Gemini Pro is still free :). But in a professional setup you would probably finetune an LLM and don't use the few-shot examples every time which makes up the largest share of tokens in the prompt.
