from unittest import TestCase
from .helper import *
import scold


class TestPraise(TestCase):

    def test_corner_case(self):
        self.assertEqual("", scold.scold(""))
        self.assertEqual("None", scold.scold(None))
        self.assertEqual("foo", scold.scold("foo"))
        self.assertEqual("${foo}", scold.scold("${foo}"))

    def test_word(self):
        self.assertTrue(
            scold.scold("${adjective}") in scold.adjective.adjective)
        self.assertTrue(scold.scold("${adverb}") in scold.adverb.adverb)
        self.assertTrue(
            scold.scold("${exclamation}") in scold.exclamation.exclamation)
        self.assertTrue(scold.scold("${smiley}") in scold.smiley.smiley)
        self.assertTrue(scold.scold("${created}") in scold.verb.created)
        self.assertTrue(scold.scold("${creating}") in scold.verb.creating)

    def test_milti_words(self):
        template = "${adjective},${adverb},${exclamation},${smiley},${created},${creating}"
        result = scold.scold(template).split(",")
        self.assertEqual(6, len(result))

        self.assertTrue(result[0] in scold.adjective.adjective)
        self.assertTrue(result[1] in scold.adverb.adverb)
        self.assertTrue(result[2] in scold.exclamation.exclamation)
        self.assertTrue(result[3] in scold.smiley.smiley)
        self.assertTrue(result[4] in scold.verb.created)
        self.assertTrue(result[5] in scold.verb.creating)

    def test_caption_words(self):
        self.assertTrue(caption_check(scold.scold("${ADJECTIVE}"), scold.adjective.adjective))
        self.assertTrue(caption_check(scold.scold("${ADVERB}"), scold.adverb.adverb))
        self.assertTrue(caption_check(scold.scold("${EXCLAMATION}"), scold.exclamation.exclamation))
        self.assertTrue(caption_check(scold.scold("${SMILEY}"), scold.smiley.smiley))
        self.assertTrue(caption_check(scold.scold("${CREATED}"), scold.verb.created))
        self.assertTrue(caption_check(scold.scold("${CREATING}"), scold.verb.creating))

    def test_first_caption_words(self):
        self.assertTrue(first_letter_caption_check(scold.scold("${Adjective}"), scold.adjective.adjective))
        self.assertTrue(first_letter_caption_check(scold.scold("${Adverb}"), scold.adverb.adverb))
        self.assertTrue(first_letter_caption_check(scold.scold("${Exclamation}"), scold.exclamation.exclamation))
        self.assertTrue(first_letter_caption_check(scold.scold("${Smiley}"), scold.smiley.smiley))
        self.assertTrue(first_letter_caption_check(scold.scold("${Created}"), scold.verb.created))
        self.assertTrue(first_letter_caption_check(scold.scold("${Creating}"), scold.verb.creating))
