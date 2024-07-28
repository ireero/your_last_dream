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
            model='gpt-4o-mini',
        )

    
    def psicologic_analises(self, dream: str) -> str:
        template = f""" Você é um guru dos sonhos, faça uma analise psicologica sobre o seguinte sonho: {dream}.
                            Responda somente com a analise, nada mais.
                        """
        final_text_result = self.llm.invoke([
            HumanMessage(content=template)
        ]).content

        print(f'Texto analisado psicologic -> {final_text_result}')

        return final_text_result
    
    def imaginary_sugestions(self, dream: str) -> str:
        template = f"""Aqui está o sonho desta pessoa: {dream}.
                        Preciso que você aponte ao menos 5 idéias criativas para esta pessoa.
                            Apresente uma lista numerada com cada ideia e o motivo da ideia estar relacionada ao sonho.
                        
                            Formate o texto usando markdown.
                        """
        final_text_result = self.llm.invoke(
            [
                HumanMessage(content=template)
            ]
        ).content

        print(f'Texto analisado resume -> {final_text_result}')

        return final_text_result
    
    def resume_analises(self, dream: str) -> str:
        template = f"""Faça um resumo deste sonho: {dream}.
                            A idéia é que será um resumo para falar para a própia pessoa o que ela sonhou. Seja prático falando o que ela sonhou e não opine sobre nada.
                        """
        final_text_result = self.llm.invoke(
            [
                HumanMessage(content=template)
            ]
        ).content

        print(f'Texto analisado resume -> {final_text_result}')

        return final_text_result