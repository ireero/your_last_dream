from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain_core.messages import HumanMessage, AIMessage

class LLM:

    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            temperature=0,
            model='gpt-3.5-turbo',
        )

    
    def psicologic_analises(self, dream: str) -> str:
        template = f""" Você é um guru dos sonhos, faça uma analise psicologica sobre o seguinte sonho: {dream}.
                            Responda somente com a analise, nada mais.
                        """
        final_text_result = self.llm.invoke([
            HumanMessage(content=template)
        ]).content

        print(f'Texto analisado -> {final_text_result}')

        return final_text_result