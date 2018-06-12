from ..base.base_result_translator import BaseResultTranslator


class DummyResultTranslator(BaseResultTranslator):

    def translate_results(self, data, options, mapping=None):
        """
        Takes in passed in results string and returns it
        :param data: results string that gets returned
        :type data: str
        :param mapping: This is unused
        :type mapping: str
        :return: the passed in data
        :rtype: str
        """
        # translate results...
        return data
