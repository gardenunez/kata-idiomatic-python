from kata.board import Board
from unittest import TestCase


class TestBoard(TestCase):

    def test_is_public(self):
        board = Board(title='irrelevant_title', is_public=True)
        assert isinstance(board, Board)
        assert board.is_public

    def test_is_not_public_when_false(self):
        board = Board(title='irrelevant_title', is_public=False)
        assert isinstance(board, Board)
        assert board.is_public is False

    def test_is_not_public_when_None(self):
        board = Board(title='irrelevant_title', is_public=None)
        assert isinstance(board, Board)
        assert board.is_public is False

    def test_add_tag_list(self):
        board = Board(title='irrelevant_title')
        tags = ['tag_1', 'tag_2', 'tag_3']
        board.add_tags(tags)
        assert board.tags == tags

    def test_add_single_tag(self):
        board = Board(title='irrelevant_title')
        tag = 'tag_1'
        board.add_tags(tag)
        assert board.tags == [tag]

    def test_add_none_tags(self):
        board = Board(title='irrelevant_title')
        board.add_tags('')
        board.add_tags(None)
        assert board.tags == []
