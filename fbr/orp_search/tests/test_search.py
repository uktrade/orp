import unittest

from unittest.mock import MagicMock, call, patch

from orp_search.utils.search import create_search_query


class TestCreateSearchQuery(unittest.TestCase):

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_single_word_query(self, mock_search_query):
        result = create_search_query("test")
        mock_search_query.assert_called_with("test", search_type="plain")
        self.assertEqual(result, mock_search_query.return_value)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_implicit_and_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2]

        # Call the function
        _ = create_search_query("test trial")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__and__.assert_called_once_with(mock_query2)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_multiple_implicit_and_search_operator_query(
        self, mock_search_query
    ):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")
        mock_query3 = MagicMock(name="MockQuery3")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2, mock_query3]

        # Call the function
        _ = create_search_query("test trial error")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
            call("error", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__and__.assert_called_with(mock_query3)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_and_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2]

        # Call the function
        _ = create_search_query("test AND trial")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__and__.assert_called_once_with(mock_query2)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_multiple_and_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")
        mock_query3 = MagicMock(name="MockQuery3")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2, mock_query3]

        # Call the function
        _ = create_search_query("test AND trial AND error")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
            call("error", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__and__.assert_called_with(mock_query3)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_or_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2]

        # Call the function
        _ = create_search_query("test OR trial")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__or__.assert_called_once_with(mock_query2)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_multple_or_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")
        mock_query3 = MagicMock(name="MockQuery3")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2, mock_query3]

        # Call the function
        _ = create_search_query("test OR trial OR error")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
            call("error", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__or__.assert_called_with(mock_query3)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_multiple_or_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")
        mock_query3 = MagicMock(name="MockQuery3")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2, mock_query3]

        # Call the function
        _ = create_search_query("test OR trial OR error")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
            call("error", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__or__.assert_called_with(mock_query3)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_phrase_search_query(self, mock_search_query):
        result = create_search_query('"test trial"')
        mock_search_query.assert_called_with(
            "test trial", search_type="phrase"
        )
        self.assertEqual(result, mock_search_query.return_value)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_and_multiple_single_single_phrase_search_query(
        self, mock_search_query
    ):
        mock_query1 = MagicMock(name="MockQuery1")  # word1
        mock_query2 = MagicMock(name="MockQuery2")  # word2
        mock_query3 = MagicMock(name="MockQuery3")  # "word3 word4"
        mock_query4 = MagicMock(name="MockQuery4")  # word5
        mock_query5 = MagicMock(name="MockQuery5")  # word6

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [
            mock_query1,
            mock_query2,
            mock_query3,
            mock_query4,
            mock_query5,
        ]

        _ = create_search_query(
            'word1 AND word2 AND "word3 word4" AND word5 word6'
        )

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("word1", search_type="plain"),
            call("word2", search_type="plain"),
            call("word3 word4", search_type="phrase"),
            call("word5", search_type="plain"),
            call("word6", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the AND operation was applied
        mock_query1.__and__.assert_called_with(mock_query5)

    @patch("orp_search.utils.search.SearchQuery", autospec=True)
    def test_single_or_and_search_operator_query(self, mock_search_query):
        # Mock SearchQuery instances
        mock_query1 = MagicMock(name="MockQuery1")
        mock_query2 = MagicMock(name="MockQuery2")
        mock_query3 = MagicMock(name="MockQuery3")

        # Configure the mock to return mock objects
        mock_search_query.side_effect = [mock_query1, mock_query2, mock_query3]

        # Call the function
        _ = create_search_query("test OR trial AND error")

        # Assert that SearchQuery was called with expected arguments
        calls = [
            call("test", search_type="plain"),
            call("trial", search_type="plain"),
            call("error", search_type="plain"),
        ]
        mock_search_query.assert_has_calls(calls, any_order=False)

        # Assert the OR and AND operation was applied
        mock_query1.__or__.assert_called_with(mock_query2)
        # mock_query2.__and__.assert_called_with(mock_query3) # TODO:fix assert


if __name__ == "__main__":
    unittest.main()
