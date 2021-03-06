# -*- coding: utf-8 -*-

class Dark(object):
    """Classe para o tema Dark da calculadora"""
    def __init__(self):
        self.master_bg = '#252729'
        self.frame_bg = '#252729'

        self.INPUT = {
            'bg': '#252729',
            'fg': 'white',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'bg': '#050505',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#0097e6',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'bg': '#0e0f0f',
            'fg': '#f5f6fa',
            'activebackground': '#d63031',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }


class White(object):
    """Classe para o tema White da calculadora"""
    def __init__(self):
        self.master_bg = '#f5f6fa'
        self.frame_bg = '#f5f6fa'

        self.INPUT = {
            'bg': '#f5f6fa',
            'fg': '#2d3436',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'bg': '#d4d4d4',
            'fg': '#2d3436',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'bg': '#adacac',
            'fg': '#2d3436',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'bg': '#d4d4d4',
            'fg': '#2d3436',
            'activebackground': '#0097e6',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'bg': '#d4d4d4',
            'fg': '#2d3436',
            'activebackground': '#d63031',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }


class DefaultStyleForMacOS(object):
    """Classe criada para ambientes macOS para corrigir bug de estilo."""
    def __init__(self):
        self.master_bg = ''
        self.frame_bg = ''

        self.INPUT = {
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 7,
            'height': 3,
            'font': 'Arial 14 bold'
        }


class Dracula(object):
    """Classe para o tema Dracula da calculadora"""
    def __init__(self):
        self.master_bg = '#282a36'
        self.frame_bg = '#282a36'

        self.INPUT = {
            'bg': '#282a36',
            'fg': '#f8f8f2',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'bg': '#44475a',
            'fg': '#f8f8f2',
            'activebackground': '#282a36',
            'activeforeground': '#50fa7b',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'bg': '#44475a',
            'fg': '#f8f8f2',
            'activebackground': '#282a36',
            'activeforeground': '#50fa7b',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'bg': '#44475a',
            'fg': '#f8f8f2',
            'activebackground': '#6272a4',
            'activeforeground': '#282a36',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'bg': '#44475a',
            'fg': '#f8f8f2',
            'activebackground': '#ff5555',
            'activeforeground': '#000000',
            'highlightthickness': 0,
            'borderwidth': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }


class Dark_Blue(object):
    """Classe para o tema Dark Blue da calculadora"""
    def __init__(self):
        self.master_bg = '#252729'
        self.frame_bg = '#252729'

        self.INPUT = {
            'bg': '#252729',
            'fg': 'white',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 15,
            'font': 'Arial 28 bold',
            'justify': 'right'
        }

        self.BTN_DEFAULT = {
            'bg': '#0e151f',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_NUMERICO = {
            'bg': '#0b111a',
            'fg': '#f5f6fa',
            'activebackground': '#0097e6',
            'activeforeground': '#162130',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_OPERADOR = {
            'bg': '#0e151f',
            'fg': '#f5f6fa',
            'activebackground': '#635f5f',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }

        self.BTN_CLEAR = {
            'bg': '#0e151f',
            'fg': '#f5f6fa',
            'activebackground': '#d63031',
            'activeforeground': '#000000',
            'borderwidth': 0,
            'highlightthickness': 0,
            'width': 6,
            'height': 2,
            'font': 'Arial 14 bold'
        }