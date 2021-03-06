#!/usr/bin/python

import unittest
from mock import MagicMock

class ChessTest(unittest.TestCase):
    """
    Unit tests for chess.
    """

    STARTING_BOARD = [ ['r','p','','','','','*p','*r'],
                       ['n','p','','','','','*p','*n'],
                       ['b','p','','','','','*p','*b'],
                       ['q','p','','','','','*p','*q'],
                       ['k','p','','','','','*p','*k'],
                       ['b','p','','','','','*p','*b'],
                       ['n','p','','','','','*p','*n'],
                       ['r','p','','','','','*p','*r'] ]

    """
    Board1:

                      +----+----+----+----+----+----+----+----+
                    8 | *r |    | *b |    | *k | *b | *n | *r |
                      +----+----+----+----+----+----+----+----+
                    7 |    | *p | *p | *p |    | *p |    | *p |
                      +----+----+----+----+----+----+----+----+
                    6 | *p |    | *n |    | *p |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    5 |    |    |    |  p |    |    | *p |    |
                      +----+----+----+----+----+----+----+----+
                    4 |    |  p |    |  q |    | *q |  p |    |
                      +----+----+----+----+----+----+----+----+
                    3 |  n |    |    |    |    |  n |    |    |
                      +----+----+----+----+----+----+----+----+
                    2 |  p |    |  p |    |  p |  p |    |  p |
                      +----+----+----+----+----+----+----+----+
                    1 |  r |    |  b |    |  k |  b |    |  r |
                      +----+----+----+----+----+----+----+----+

                         a    b    c    d    e    f    g    h
    """

    board1         = [ ['r','p','n',''  ,''  ,'*p',''  ,'*r'],
                       ['' ,'' ,'' ,'p' ,''  ,''  ,'*p',''  ],
                       ['b','p','' ,''  ,''  ,'*n','*p','*b'],
                       ['' ,'' ,'' ,'q' ,'p' ,''  ,'*p',''  ],
                       ['k','p','' ,''  ,''  ,'*p',''  ,'*k'],
                       ['b','p','n','*q',''  ,''  ,'*p','*b'],
                       ['' ,'' ,'' ,'p' ,'*p',''  ,''  ,'*n'],
                       ['r','p','' ,''  ,''  ,''  ,'*p','*r'] ]



    """
    Board2:

                      +----+----+----+----+----+----+----+----+
                    8 |    | *n |    |    |    |    |    | *r |
                      +----+----+----+----+----+----+----+----+
                    7 | *p |    |    |    | *k |    | *p |    |
                      +----+----+----+----+----+----+----+----+
                    6 |    |    | *b |    |    | *p |    |    |
                      +----+----+----+----+----+----+----+----+
                    5 |    |    |    |    |    |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    4 |    |    |    |  q |    |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    3 |    |  r |    |    |  n |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    2 |    |    |    |  p |    |    |    |  p |
                      +----+----+----+----+----+----+----+----+
                    1 |  k |    |  b |    |    |    |    |    |
                      +----+----+----+----+----+----+----+----+

                         a    b    c    d    e    f    g    h
    """

    board2         = [ ['k','' ,'' ,''  ,'',''  ,'*p',''  ],
                       ['' ,'' ,'r',''  ,'',''  ,''  ,'*n'],
                       ['b','' ,'' ,''  ,'','*b',''  ,''  ],
                       ['' ,'p','' ,'q' ,'',''  ,''  ,''  ],
                       ['' ,'' ,'n',''  ,'',''  ,'*k',''  ],
                       ['' ,'' ,'' ,''  ,'','*p',''  ,''  ],
                       ['' ,'' ,'' ,''  ,'',''  ,'*p',''  ],
                       ['' ,'p','' ,''  ,'',''  ,''  ,'*r'] ]


    #More boards (no illustrations given)
    board3        =  [ ['r','p','',''  ,'','','*p',''  ],
                       ['n','p','',''  ,'','','*p','*n'],
                       ['b','p','',''  ,'','','*p','*b'],
                       ['q','p','','*r','','','*p','*q'],
                       ['' ,'p','','k' ,'','','*p','*k'],
                       ['b','p','',''  ,'','','*p','*b'],
                       ['n','p','',''  ,'','','*p','*n'],
                       ['r','p','',''  ,'','','*p','*r'] ]

    check1         = [ ['r','p','*r',''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,''  ,'*p','*n'],
                       ['b','p',''  ,''  ,''  ,'*q','*p','*b'],
                       ['q','' ,''  ,'p' ,''  ,''  ,'*p',''  ],
                       ['' ,'' ,'p' ,'k' ,''  ,''  ,'*p','*k'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['r','p','*r',''  ,''  ,''  ,''  ,''  ] ]

    check2         = [ ['' ,'p',''  ,''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,''  ,'*p','*n'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['q','p','r' ,''  ,''  ,''  ,'*p','*q'],
                       ['k','p','r' ,''  ,'*k',''  ,'*p',''  ],
                       ['b','' ,''  ,'p' ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['' ,'p',''  ,''  ,''  ,''  ,''  ,''  ] ]

    checkmate1     = [ ['r','p','*r',''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,''  ,'*p','*n'],
                       ['b','p',''  ,''  ,''  ,'*q','*p','*b'],
                       ['q','p' ,'' ,'k' ,''  ,''  ,'*p',''  ],
                       ['' ,'p',''  ,''  ,''  ,''  ,'*p','*k'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['r','p',''  ,''  ,'*r',''  ,''  ,''  ] ]

    checkmate2     = [ ['' ,'' ,'' ,'' ,''  ,''  ,'*b',''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,'q' ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,'*k',''  ,''],
                       ['' ,'' ,'' ,'' ,'p' ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,'r' ,''],
                       ['' ,'' ,'' ,'' ,''  ,'r' ,''  ,''] ]

    def setUp(self):
        """
        Setup test fixture.
        """
        pass

    def tearDown(self):
        """
        Tear down test fixture.
        """
        pass

    ########################
    # Tests for Game class #
    ########################

    def test_game_initialization(self):
        from game import Game
        import constants

        g = Game()
        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)

    #Tests for _nextTurn()

    def test_next_turn_switching_players(self):
        from game import Game
        import constants

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")
       
        #Mock-up board functions
        b = g._board
        b._isLegalMove = MagicMock(return_value=True)
        b.isCheck      = MagicMock(return_value=False)
        b.isCheckMate  = MagicMock(return_value=False)

        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)
        g._nextTurn()
        self.assertEqual(g._currentPlayer, constants.BLACK_PLAYER)

    def test_next_turn_process(self):
        from game import Game
        import constants

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")

        #Mock-up board functions
        b = g._board
        b.isLegalMove = MagicMock(return_value=True)

        self.assertFalse(b.isLegalMove.called)
        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)

        g._nextTurn()

        b.isLegalMove.assert_called_with(constants.WHITE_PLAYER, [1, 0, 2, 2])

        self.assertEqual(g._currentPlayer, constants.BLACK_PLAYER)


    #########################
    # Tests for Board class #
    #########################

    def test_board_initialization(self):
        from board import Board
        b = Board()

        self.assertEqual(b._board, ChessTest.STARTING_BOARD)

    #Test for getBoard()

    def test_get_board(self):
        from board import Board 

        b = Board()
        self.assertEqual(b.getBoard(), ChessTest.STARTING_BOARD)

    #Tests for movePiece()

    """
    def test_move_piece_white_knight(self):
        from board import Board
        b = Board()
       
        self.assertEqual(b._board[1][0], "n")
        b.movePiece("b1c3") 
        self.assertEqual(b._board[1][0], "")
        self.assertEqual(b._board[2][2], "n")

    def test_move_piece_black_pawn(self):
        from board import Board
        b = Board()
       
        self.assertEqual(b._board[4][6], "*p")
        b.movePiece("e7e6") 
        self.assertEqual(b._board[4][6], "")
        self.assertEqual(b._board[4][5], "*p")

    def test_move_piece_queen_overtakes_queen(self):
        from board import Board
        b = Board()
        b._board      = ChessTest.board1
       
        self.assertEqual(b._board[3][3], "q")
        self.assertEqual(b._board[5][3], "*q")
        b.movePiece("d4f4") 
        self.assertEqual(b._board[3][3], "")
        self.assertEqual(b._board[5][3], "q")
    """

    #Tests for isLegalMove()
    
    """
    def test_is_legal_move(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward one space
        self.assertTrue(b.isLegalMove("d2d3", constants.WHITE_PLAYER))
        
        #Rook - move forward several spaces
        self.assertTrue(b.isLegalMove("h8h4", constants.BLACK_PLAYER))

        #Rook - move across several spaces
        self.assertTrue(b.isLegalMove("h8d8", constants.BLACK_PLAYER))

        #Knight - move forward and right
        self.assertTrue(b.isLegalMove("e3f5", constants.WHITE_PLAYER))

        #Knight - move left and up
        self.assertTrue(b.isLegalMove("b8d7", constants.BLACK_PLAYER))

        #Bishop - move diagnoally left
        self.assertTrue(b.isLegalMove("c1a3", constants.WHITE_PLAYER))

        #Bishop - move back and right
        self.assertTrue(b.isLegalMove("c6b7", constants.BLACK_PLAYER))

        #Queen - move right one space
        self.assertTrue(b.isLegalMove("d4e4", constants.WHITE_PLAYER))

        #Queen - move left several spaces
        self.assertTrue(b.isLegalMove("d4b4", constants.WHITE_PLAYER))

        #Queen - move left diagonally
        self.assertTrue(b.isLegalMove("d4b6", constants.WHITE_PLAYER))

        #King - move forward
        self.assertTrue(b.isLegalMove("e7e6", constants.BLACK_PLAYER))

        #King - move backward 
        self.assertTrue(b.isLegalMove("e7e8", constants.BLACK_PLAYER))

        #King - move left 
        self.assertTrue(b.isLegalMove("e7f7", constants.BLACK_PLAYER))

        #King - move right 
        self.assertTrue(b.isLegalMove("e7d7", constants.BLACK_PLAYER))

        #King - move right diagonally 
        self.assertTrue(b.isLegalMove("e7d6", constants.BLACK_PLAYER))

    def test_is_legal_move_improper_movement(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward three
        self.assertFalse(b.isLegalMove("h2h5", constants.WHITE_PLAYER))

        #Pawn - move left
        self.assertFalse(b.isLegalMove("g7h7", constants.BLACK_PLAYER))

        #Pawn - move backwards
        self.assertFalse(b.isLegalMove("d2d1", constants.WHITE_PLAYER))

        #Rook - move diagonally
        self.assertFalse(b.isLegalMove("b3c4", constants.WHITE_PLAYER))

        #Knight - move forward two
        self.assertFalse(b.isLegalMove("e3e5", constants.WHITE_PLAYER))

        #Bishop - move forward one
        self.assertFalse(b.isLegalMove("c1c2", constants.WHITE_PLAYER))

        #Queen - move like knight
        self.assertFalse(b.isLegalMove("d4b5", constants.WHITE_PLAYER))

        #King - move forward two
        self.assertFalse(b.isLegalMove("e7e5", constants.BLACK_PLAYER))

    def test_is_legal_move_piece_not_moved(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        self.assertFalse(b.isLegalMove("c1c1", constants.WHITE_PLAYER))

    def test_is_legal_move_moving_into_occupied_space(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #White rook moves into white pawn
        self.assertFalse(b.isLegalMove("a1a2", constants.WHITE_PLAYER))

        #Black king moves into black bishop
        self.assertFalse(b.isLegalMove("e8f8", constants.BLACK_PLAYER))

    def test_is_legal_move_legal_kills(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #White knight kills black pawn
        self.assertTrue(b.isLegalMove("f3g5", constants.WHITE_PLAYER))

        #Black queen kills white bishop
        self.assertTrue(b.isLegalMove("f4c1", constants.BLACK_PLAYER))

        #White bishop kills black queen
        self.assertTrue(b.isLegalMove("c1f4", constants.WHITE_PLAYER))

    def test_is_legal_move_blocked_move(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #Pawn tries to move forward two spaces, is blocked by knight
        self.assertFalse(b.isLegalMove("a2a4", constants.WHITE_PLAYER))

        #Rook tries to move forward, is blocked by pawn
        self.assertFalse(b.isLegalMove("h8h5", constants.BLACK_PLAYER))

        #Rook tries to move across, is blocked by several pieces
        self.assertFalse(b.isLegalMove("h8d8", constants.BLACK_PLAYER))

        #Knight 'jumps' - can't be blocked by any pieces

        #Bishop tries to move left diagonally, is blocked by pawn
        self.assertFalse(b.isLegalMove("f1c4", constants.WHITE_PLAYER))

        #Queen tries to move across, is blocked by other queen
        self.assertFalse(b.isLegalMove("f4c4", constants.BLACK_PLAYER))

        #King can only move one space at a time

    def test_is_legal_move_illegal_kills(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #Black pawn moves forward to kill white pawn
        self.assertFalse(b.isLegalMove("g5g4", constants.BLACK_PLAYER))

        #Knight moves forward three spaces to kill black pawn
        self.assertFalse(b.isLegalMove("a3a6", constants.WHITE_PLAYER))
    """

    #Tests for _isLegalMoveForPawn()

    """
    def test_is_legal_move_for_pawn(self):
        from board import Board

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn("h2h3"))
        
        #White pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn("h2h4"))

        #Black pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn("g7g6"))
        
        #Black pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn("g7g5"))

        #Black pawn, forward one space from non-default position
        self.assertTrue(b._isLegalMoveForPawn("f6f5"))

        b._board = ChessTest.board1
    
        #Legal move to kill
        self.assertTrue(b._isLegalMoveForPawn("d5e6"))

        #Legal move to kill 2
        self.assertTrue(b._isLegalMoveForPawn("d5c6"))

    def test_is_legal_move_for_pawn_negative_test(self):
        from board import Board

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward three spaces from default position
        self.assertFalse(b._isLegalMoveForPawn("h2h5"))
        
        #White pawn, backward one space 
        self.assertFalse(b._isLegalMoveForPawn("h2h1"))

        #Black pawn, move to left 
        self.assertFalse(b._isLegalMoveForPawn("f6g6"))
        
        #Black pawn, move to right 
        self.assertFalse(b._isLegalMoveForPawn("f6e6"))
        
        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn("f6e5"))

        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn("f6g5"))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn("h2g1"))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn("d2e1"))

        #White pawn, far across board 
        self.assertFalse(b._isLegalMoveForPawn("d2f8"))

        b._board = ChessTest.board1

        #Cannot kill piece by moving forward (must move diagnoally)
        self.assertFalse(b._isLegalMoveForPawn("g4g5"))
        
    """

    # Tests for isLegalMoveForRook()

    """
    def test_is_legal_move_for_rook(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Left
        self.assertTrue(b._isLegalMoveForRook("b3a3"))
        
        #Right
        self.assertTrue(b._isLegalMoveForRook("b3d3"))

        #Up
        self.assertTrue(b._isLegalMoveForRook("b3b7"))

        #Down
        self.assertTrue(b._isLegalMoveForRook("h8h4"))

        #Legal kill
        self.assertTrue(b._isLegalMoveForRook("b3b8"))

    def test_is_legal_move_for_rook_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Diagnoal
        self.assertFalse(b._isLegalMoveForRook("b3a4"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForRook("h8a8"))

        #Path blocked by enemy piece
        self.assertFalse(b._isLegalMoveForRook("h8h1"))
    """

    # Tests for isLegalMoveForKnight()
    
    """
    def test_is_legal_move_for_knight(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Forward and right
        self.assertTrue(b._isLegalMoveForKnight("e3f5"))
        
        #Forward and left
        self.assertTrue(b._isLegalMoveForKnight("e3d5"))

        #Right and up
        self.assertTrue(b._isLegalMoveForKnight("e3g4"))

        #Left and down
        self.assertTrue(b._isLegalMoveForKnight("e3c2"))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForKnight("f3g5"))

    def test_is_legal_move_for_knight_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left two
        self.assertFalse(b._isLegalMoveForKnight("f3d3"))
    """

    # Tests for isLegalMoveForBishop()

    """
    def test_is_legal_move_for_bishop(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Move up and to the left
        self.assertTrue(b._isLegalMoveForBishop("c1a3"))
        
        #Move down and to the right
        self.assertTrue(b._isLegalMoveForBishop("c6e8"))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForBishop("f8b4"))

    def test_is_legal_move_for_bishop_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertFalse(b._isLegalMoveForBishop("c8b8"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForBishop("f1d3"))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForBishop("f8a3"))
    """

    # Tests for isLegalMoveForQueen()
    
    """
    def test_is_legal_move_for_queen(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForQueen("f4e4"))

        #Move right
        self.assertTrue(b._isLegalMoveForQueen("d4e4"))

        #Move up and left
        self.assertTrue(b._isLegalMoveForQueen("d4a7"))

        #Move down and right
        self.assertTrue(b._isLegalMoveForQueen("f4g3"))

        #Legal kill
        self.assertTrue(b._isLegalMoveForQueen("f4h2"))

        #Legal kill2
        self.assertTrue(b._isLegalMoveForQueen("d4f4"))

        #Legal kill3
        self.assertTrue(b._isLegalMoveForQueen("f4c1"))

    def test_is_legal_move_for_queen_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move like horse
        self.assertFalse(b._isLegalMoveForQueen("d4f5"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForQueen("f4g6"))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForQueen("f4b4"))
    """

    # Tests for isLegalMoveForKing()

    """
    def test_is_legal_move_for_king(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForKing("e8d8"))

        #Move up and left 
        self.assertTrue(b._isLegalMoveForKing("e1d2"))

        #Move down 
        self.assertTrue(b._isLegalMoveForKing("e8e7"))

        b._board = ChessTest.board3

        #Legal kill
        self.assertTrue(b._isLegalMoveForKing("e4d4"))

    def test_is_legal_move_for_king_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move diagnoally two spaces
        self.assertFalse(b._isLegalMoveForKing("e1c3"))
    """

    #################################
    # Tests for BoardAnalyzer class #
    #################################

    #Tests for isCheckMate()

    """
    def test_is_check_mate(self):
        import board_analyer

        self.assertTrue(board_analyzer.isCheckMate(ChessTest.checkmate1, constants.WHITE_PLAYER))
        self.assertTrue(board_analyzer.isCheckMate(ChessTest.checkmate2, constants.BLACK_PLAYER))

    def test_is_check_mate_negative(self):
        import board_analyer

        self.assertFalse(board_analyzer.isCheckMate(ChessTest.board1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.board1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.board2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.board2, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.check1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.check1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.check2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(ChessTest.check2, constants.BLACK_PLAYER))
    """

    #Tests for isCheck()

    """
    def test_is_check(self):
        import board_analyer
    
        self.assertTrue(board_analyzer.isCheck(ChessTest.check1, constants.WHITE_PLAYER))
        self.assertTrue(board_analyzer.isCheck(ChessTest.check2, constants.BLACK_PLAYER))
        
    def test_is_check_negative(self):
        import board_analyer

        self.assertFalse(board_analyzer.isCheck(ChessTest.board1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheck(ChessTest.board1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheck(ChessTest.board2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheck(ChessTest.board2, constants.BLACK_PLAYER))
    """

if __name__ == '__main__':
    unittest.main()
