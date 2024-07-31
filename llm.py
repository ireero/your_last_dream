from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from flask import session

class LLM:
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            temperature=0,
            model='gpt-4o-mini',
        )

    def invoke_llm(self, template: str) -> str:
        return self.llm.invoke([HumanMessage(content=template)]).content

    def personal_characteristics_characteristics_on_profession(self, profession: str) -> str:
        template = f"""
        Responda com possíveis características de personalidade de uma pessoa com base na profissão {profession}, 
        responda somente com as características e suas respectivas explicações.
        """
        result = self.invoke_llm(template)
        print(f'Texto analisado personal -> {result}')
        return result

    def psicologic_analises(self, dream: str) -> str:
        template = f"""
        Você é um guru dos sonhos, faça uma análise psicológica sobre o seguinte sonho: {dream}.
        Responda somente com a análise, nada mais.
        """
        result = self.invoke_llm(template)
        print(f'Texto analisado psicologic -> {result}')
        return result

    def imaginary_sugestions(self, dream: str) -> str:
        user_profession = session.get('user_profession')
        characteristics = self.personal_characteristics_characteristics_on_profession(user_profession)
        template = f"""
        Aqui está o sonho desta pessoa: {dream}.
        Sabendo que a pessoa é {user_profession} e tem as possíveis características em sua personalidade: {characteristics}.
        Preciso que você aponte ao menos 5 ideias criativas para esta pessoa.
        Apresente uma lista numerada com cada ideia e o motivo da ideia estar relacionada ao sonho.
        Formate o texto usando markdown.
        """
        result = self.invoke_llm(template)
        print(f'Texto analisado resume -> {result}')
        return result

    def resume_analises(self, dream: str) -> str:
        template = f"""
        Faça um resumo deste sonho: {dream}.
        A ideia é que será um resumo para falar para a própria pessoa o que ela sonhou. Seja prático falando o que ela sonhou e não opine sobre nada.
        """
        result = self.invoke_llm(template)
        print(f'Texto analisado resume -> {result}')
        return result

    def profession_verification(self, profession: str) -> str:
        template = f"""
        O usuário afirmou que isso é sua profissão: {profession}.
        Responda com a profissão desse usuário.
        Caso o usuário esteja dando a entender que não trabalha, retorne o texto "desempregado".
        Caso a profissão do usuário seja desconhecida, responda com somente "desconhecido".
        Responda somente com a profissão do usuário e nada mais.
        """
        result = self.invoke_llm(template)
        print(f'Texto analisado verification -> {result}')
        return result
