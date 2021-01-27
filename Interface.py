# coding: utf-8
import pandas as pd
import random
import my_linked_list
import my_tree
import my_queue
import my_stack
import my_graph
from tkinter import *
from tkinter import messagebox
from turtle_tree import *

match = pd.read_csv('match.csv')
country = pd.read_csv('country.csv')
league = pd.read_csv('league.csv')
player = pd.read_csv('player.csv')
player_attributes = pd.read_csv('player_attributes.csv')
team = pd.read_csv('team.csv')
team_attributes = pd.read_csv('team_attributes.csv')
# graph
data = pd.read_csv('gender-classifier-DFE-791531.csv', encoding='latin1')

# ######################################################################################################################
# ###FUNCTIONS RELATED WITH THE COMMANDS OF THE BUTTONS OF THE DATA STRUCTURE'S WINDOWS### #############################
# ######################################################################################################################

# ###FUNCTIONS USED TO GET RANDOM NUMBERS IN THE LENGTH OF THE DATASETS### #............................................

# LIST, QUEUE, STACK, TREE
def get_randoms(data):
    # This function returns an aleatory int smaller than the length of the dataset

    # Get the length of the dataset
    l = len(data['id']) - 1

    # Return an aleatory int
    return random.randint(0, l)


# GRAPH
def get_randoms_graph(data):
    # This function returns an aleatory int smaller than the length of the dataset

    # Get the length of the dataset
    l = len(data['_unit_id']) - 1

    # Return an aleatory int
    return random.randint(0, l)


# ###FUNCTIONS USED TO SHOW ERROR MESSAGES BOX IN THE CODE### #.........................................................


# TRY TO MANIPULATE THE DATA STRUCTURE WITHOUT GENERATE IT
def error_1(list_box, janela):
    if list_box.size() == 0:
        messagebox.showerror("Estrutura vazia!", "Crie a estrutura para poder manipular os itens!", parent = janela)
        return -1

    return 0


# TRY TO GENERATE THE DATA STRUCTURE WITHOUT SPECIFY THE SIZE OF IT
def error_2(n, janela):
    if n == "":
        messagebox.showerror("Sem quantidade de elementos!", "Defina a quantidade de elementos da estrutura "
                                                             "para gerá-la!", parent = janela)
        return -1

    return 0


# ERROR TREATMENT REGARDING THE DISTANCE GRAPH OPERATION
def error_3(v1, v2, list_box, janela):
    if v1 == '' or v2 == '':
        messagebox.showerror("Vetores não definidos!", "Você não especificou os vetores necessários para "
                                                       "essa operação!", parent = janela)
        return -1
    else:
        i = 0
        x = 0
        n = list_box.size()
        while i < n:
            s = list_box.get(i)
            if v1 == s[2]:
                list_box.activate(i)
                list_box.see(i)
                x += 1
            i += 1
        i = 0
        while i < n:
            s = list_box.get(i)
            if v2 == s[2]:
                list_box.activate(i)
                list_box.see(i)
                x += 2
            i += 1
        if x == 0:
            messagebox.showerror("Vetores ausentes", "Nenhum dos vetores indicados está presente no grafo!",
                                 parent=janela)
            return -1
        if x == 1:
            messagebox.showerror("Vetor ausente", "O segundo vetor não se encontra no grafo!",
                                 parent=janela)
            return -1
        if x == 2:
            messagebox.showerror("Vetores ausentes", "O primeiro vetor não se encontra no grafo!",
                                 parent=janela)
            return -1
        return 0


# ###SEARCH FUNCTION FOR SEARCHING NODES IN THE TREE AND THE GRAPH### #.................................................
def search(element, list_box, window):
    error_1(list_box, window)
    i = 0
    x = 0
    n = list_box.size()
    while i < n:
        s = list_box.get(i)
        if element == s[2]:
            list_box.activate(i)
            list_box.see(i)
            x = 1
        i += 1
    if x == 0 and n != 0:
        messagebox.showerror("Elemento não encontrado!", "O elemento procurado não se encontra na estrutura."
                                                         " Certifique-se de que o digitou corretamente!",
                             parent = window)


# ###FUNCTIONS FOR EACH STRUCTURE'S INFO BUTTON### #....................................................................
# these functions create a text box that shows details about the select nodes, according to each data structure
# integrity

# LIST
def info_list(element, window, list_box):
    if error_1(list_box, window) == 0:
        pos  = (lista.findPosition(int(element[2])))
        cur  = lista.get(pos)
        next = "None"
        times = (cur.away_team_name + " |VS| " + cur.home_team_name)
        dados = ("Partida:\n" + times + "\nEstádio: " + str(cur.stage) +
                 "\nTemporada: " + str(cur.season) + "\nData: " + str(cur.date))
        if (pos + 1) < list_box.size():
            nxt = (lista.get_next(pos))
            next = str(nxt.data.match_api_id)

        text = ("Posição do Nó: " + str(pos + 1) + "\n\nTamanho da Lista:" + str(lista.size()) +
                "\n\nDados Armazenados no Nó:\n\n" + dados + "\n\nPróximo nó: " + next)
        info_element = Text(window, font="Times 12", height=20, width=40)
        info_element.insert(END, ("ID da Partida: " + str(element[2]) + "\n" + text))
        info_element.grid(row = 1, column = 3)


# QUEUE
def info_queue(element, window, list_box):
    if error_1(list_box, window) == 0:
        head = fila.get(0)
        tail = fila.get(fila.getSize() - 1)
        next = "None"


        times = (head.away_team_name + " |VS| " + head.home_team_name)
        dados = ("Partida:\n" + times + "\nEstádio: " + str(head.stage) +
                 "\nTemporada: " + str(head.season) + "\nData: " + str(head.date))
        if fila.getSize() > 1:
            nxt = fila.get_next(0)
            next = str(nxt.match_api_id)


        text = ("Tamanho da fila: " + str(fila.getSize()) + "\n\nDados Armazenados:\n\n" + dados + "\n\nPróximo item: "
                + next + "\n\nCalda da fila: " + str(tail.match_api_id))
        info_element = Text(window, font="Times 12", height=20, width=40)
        info_element.insert(END, ("ID da Partida: " + str(element[2]) + "\n" + text))
        info_element.grid(row = 1, column = 3)


# STACK
def info_stack(element, window, list_box):
    if error_1(list_box, window) == 0:
        top  = pilha.peek()


        times = (top.away_team_name + " |VS| " + top.home_team_name)
        dados = ("Partida:\n" + times + "\nEstádio: " + str(top.stage) + "\nTemporada: " + str(top.season) +
                 "\nData: " + str(top.date))


        text = ("Tamanho da pilha: " + str(pilha.getSize()) + "\n\nDados Armazenados:\n\n" + dados)
        info_element = Text(window, font="Times 12", height=20, width=40)
        info_element.insert(END, ("ID da Partida: " + str(element[2]) + "\n" + text))
        info_element.grid(row = 1, column = 3)


# TREE
def info_tree(element, window, n, list_box):
    if error_1(list_box, window) == 0:
        arvore.getNode(int(element[2]))
        print((arvore.bnode.data.match_api_id))
        left_son  = "None"
        right_son = "None"
        parent    = "None"
        final = ""

        if arvore.bnode.left != None:
            left_son  = str(arvore.bnode.left.data.match_api_id)

        if arvore.bnode.right != None:
            right_son = str(arvore.bnode.right.data.match_api_id)

        if int(element[0]) != 0:
            parent = str(arvore.bnode.parent.data.match_api_id)

        if parent == "None":
            final = "\nEsse nó é a raiz da árvore."

        if left_son == "None" and right_son == "None":
            final = "\nEsse nó é uma folha da árvore."

        times = (arvore.bnode.data.away_team_name + " |VS| " + arvore.bnode.data.home_team_name)
        dados = ("Partida:\n" + times + "\nEstádio: " + str(arvore.bnode.data.stage) + "\nTemporada: " +
                 str(arvore.bnode.data.season) + "\nData: " + str(arvore.bnode.data.date))
        arvore_info = ("Nó: " + str(element[2]) + "\nPai: " + parent +
                       "\nFilho esquerdo: " + left_son + "\nFilho direito: " + right_son + final)

        text = ("Tamanho da árvore: " + str(n)  + "\n\nDados Armazenados:\n\n" + dados)
        info_element = Text(window, font="Times 12", height=20, width=40)
        info_element.insert(END, (arvore_info + "\n\nID da Partida: " + str(element[2]) + "\n" + text))
        info_element.grid(row = 1, column = 3)


# GRAPH
def info_graph(element, window, list_box):
    if error_1(list_box, window) == 0:
        cur      = grafo.get_node(int(element[2]))
        nome     = "\nNome de Usuário: " + str(cur.name)
        genero   = "\nGênero: " + str(cur.gender)
        tweets   = "\nNúmero de Tweets: " + str(cur.tweet_count)
        location = "\nLocalização: " + str(cur.tweet_location)
        favs     = "\nNúmero de Favoritos: " + str(cur.fav_number)
        retweets = "\nNúmero de retweets: " + str(cur.retweet_count)
        tz       = "\nFuso Horário: " + str(cur.user_timezone) + "\n"
        desc     = "\nDescrição: " + str(cur.description) + "\n"
        disc     = grafo.graph[cur]
        conex    = ""
        for i in disc:
            conex = (conex + "  " + str(i.unit_id))

        dados = (nome + genero + desc + location + tz + tweets + retweets + favs)

        info_element = Text(window, font = "Times 12", height = 20, width = 40)
        info_element.insert(END, ("VETOR " + str(cur.unit_id) + "\n\n####CONEXÕES####\n\n" + conex +
                                  "\n\n####DADOS SALVOS NO NÓ####\n" + dados))
        info_element.grid(row = 1, column = 3)

# ###LISTBOX FUNCTIONS### #.............................................................................................
# Functions concerned about the manipulation buttons of data structure

# LIST AND QUEUE


# Remove elements for the queue and modifies the listbox
def rmv_queue(list_box, i, n, window):
    if error_1(list_box, window) == 0:
        fila.dequeue()
        list_box.delete(0, END)

        while i < n:
            list_box.insert(END, (i, ":", fila.get(i).match_api_id))
            i += 1


# Remove elements for the list and modifies the listbox
def rmv_list(list_box, removed, i, n, window):
    if error_1(list_box, window) == 0:
        lista.pop_if(int(removed[2]))

        list_box.delete(0, END)
        while i < n:
            list_box.insert(END, (i, ":", lista.get(i).match_api_id))
            i += 1


# Generates list or queue and theirs list boxes
def crt_list_queue(list_box, m, ds, window):
    if error_2(m, window) == 0:
        n = int(m)
        i = 0
        list_box.delete(0, END)
        if ds == 1:
            global lista
            lista = my_linked_list.Linked_list()

            # Put the data in the list
            for x in range(n):
                lista.push(my_linked_list.Data_match(match, get_randoms(match)))

            while i < n:
                list_box.insert(END, (i, ":", lista.get(i).match_api_id))
                i += 1
        else:
            # Create the queue
            global fila
            fila = my_queue.Queue()

            # Put the data in the queue
            for x in range(n):
                fila.enqueue(my_queue.Data_match(match, get_randoms(match)))

            while i < n:
                list_box.insert(END, (i, ":", fila.get(i).match_api_id))
                i += 1


# Add new elements to the list or queue and their list boxes
def add_list_queue(list_box, m, ds, window):
    if error_1(list_box, window) == 0:
        n = int(m)
        i = 0
        list_box.delete(0, END)
        if ds == 1:
            # Put the data in the list
            for x in range(n):
                lista.push(my_linked_list.Data_match(match, get_randoms(match)))

            while i < lista.size():
                list_box.insert(END, (i, ":", lista.get(i).match_api_id))
                i += 1
        else:
            # Put the data in the queue
            for x in range(n):
                fila.enqueue(my_queue.Data_match(match, get_randoms(match)))

            while i < fila.getSize():
                list_box.insert(END, (i, ":", fila.get(i).match_api_id))
                i += 1


# STACK

# Remove elements for the stack and modifies the listbox
def rmv_stack(list_box, i, n, window):
    if error_1(list_box, window) == 0:
        pilha.pop()
        list_box.delete(0, END)
        m = n-1
        while i < n:
            list_box.insert(i, (m, ":", my_stack.get(pilha, i).match_api_id))
            i += 1
            m -= 1


# Generates stack and the list box with the elements of the stack
def crt_stack(list_box, l, window):
    # Put the data in the queue
    if error_2(l, window) == 0:
        n = int(l)
        list_box.delete(0, END)
        i = 0
        m = n - 1

        global pilha
        pilha = my_stack.Stack()

        # Put the data in the stack
        for x in range(n):
            pilha.push(my_stack.Data_match(match, get_randoms(match)))

        while i < n:
            list_box.insert(i, (m, ":", my_stack.get(pilha, i).match_api_id))
            i += 1
            m -= 1


# Add new element to the stack and shows it at the list box
def add_stack(list_box, l, window):
    # Put the data in the queue
    if error_1(list_box, window) == 0:
        n = int(l)
        list_box.delete(0, END)
        i = 0
        m = (pilha.getSize() + n) - 1

        # Put the data in the stack
        for x in range(n):
            pilha.push(my_stack.Data_match(match, get_randoms(match)))

        while i < pilha.getSize():
            list_box.insert(i, (m, ":", my_stack.get(pilha, i).match_api_id))
            i += 1
            m -= 1


# TREE

# Sort the tree according to a new parameter for construction and generates the new listbox
def srt_tree(list_box, parameter, window):
    if error_1(list_box, window) == 0:
        list_box.delete(0, END)
        global count_tree
        count_tree = 0
        #arvore.sortTree(parameter)
        arvore.sortTree(parameter)

        interfaceTree(arvore.root, list_box)


# Walks trough every element for the tree and inserts them in the listbox
def interfaceTree(cur, list_box):
    if cur != None:
        global count_tree
        if count_tree == 0:
            list_box.insert(END, (count_tree, ":", cur.data.match_api_id, "(ROOT)"))
        else:
            list_box.insert(END, (count_tree, ":", cur.data.match_api_id))
        count_tree += 1
        interfaceTree(cur.left, list_box)
        interfaceTree(cur.right, list_box)


# Generates tree and the list box with the elements of the tree
def crt_tree(list_box, m, window):
    if error_2(m, window) == 0:
        n = int(m)
        list_box.delete(0, END)
        # Create the tree
        global arvore, count_tree
        arvore = my_tree.BinaryTree()
        count_tree = 0

        # Put the data in the tree
        for x in range(n):
            arvore.insert(my_tree.Data_match(match, get_randoms(match)))

        interfaceTree(arvore.root, list_box)


# Remove elements for the tree and modifies the listbox
def rmv_tree(list_box, removed, window):
    if error_1(list_box, window) == 0:
        global count_tree
        count_tree = 0
        arvore.delete(int(removed[2]))
        list_box.delete(0, END)

        interfaceTree(arvore.root, list_box)


# Add element to the tree
def add_tree(list_box, m, window):
    if error_1(list_box, window) == 0:
        n = int(m)
        list_box.delete(0, END)
        # Create the tree)

        # Put the data in the tree
        for x in range(n):
            arvore.insert(my_tree.Data_match(match, get_randoms(match)))
        global count_tree
        count_tree = 0
        interfaceTree(arvore.root, list_box)


# GRAPH

# Generates graph and the list box with the elements of the graph
def crt_graph(list_box, m, window):
    if error_2(m, window) == 0:
        n = int(m)
        i = 0
        global grafo
        grafo = my_graph.Graph()


        for x in range(n):
            grafo.add(my_graph.Profile_data(data, get_randoms_graph(data)))

        list_box.delete(0, END)
        for n in grafo.nodes:
            list_box.insert(END, (i, ":", n.unit_id))
            i += 1


# Add element to the graph
def add_graph(list_box, m, window):
    if error_1(list_box, window) == 0:
        n = int(m)
        i = 0

        for x in range(n):
            grafo.add(my_graph.Profile_data(data, get_randoms_graph(data)))

        list_box.delete(0, END)
        for n in grafo.nodes:
            list_box.insert(END, (i, ":", n.unit_id))
            i += 1


# Generates the label using the user's parameters in the method short.path()
def path_gen(window, v1, v2, list_box):
    if error_1(list_box, window) == 0:

        if error_3(v1, v2, list_box, window) != -1:
            text_label = grafo.short_path_if(int(v1), int(v2))

            path_label = Label(window, bg = "#363636", fg = "white", font = "Times 12", wraplength = 400,
                               relief = "raised", bd = 5, text = text_label)
            fillabel10 = Label(window, bg = "#363636", font ="Times 12")
            fillabel10.grid(row = 8, column = 0)
            path_label.grid(row = 7, column = 1)


# Generates the window where the user can discover the shortest path for the graph
def shortest_dist(list_box):
    sp_window = Tk()
    sp_window['bg'] = "#363636"
    sp_window.title("Menor Distância")
    sp_window.iconbitmap("icons/sp_icon.ico")
    sp_window.resizable(False, False)

    label_1  = Label(sp_window, text = "\nPrimeiro vetor:  ",
                   font = "Times 12", bg = "#363636", fg = "white")
    vector_1 = Entry(sp_window, font="Times 12", width = 20)
    label_2  = Label(sp_window, text = "Segundo vetor:  ",
                    font = "Times 12", bg = "#363636", fg = "white")
    vector_2 = Entry(sp_window, font = "Times 12", width = 20)
    submit   = Button(sp_window, font = "Times 12", bg = "#363636", fg = "white", text = "Menor distância",
                      command = lambda: path_gen(sp_window, vector_1.get(), vector_2.get(), list_box))

    fillabel1 = Label(sp_window, bg = "#363636", width = 2)
    fillabel2 = Label(sp_window, bg = "#363636", width = 2)
    fillabel3 = Label(sp_window, bg = "#363636", width = 2)
    fillabel4 = Label(sp_window, bg = "#363636", width = 2)

    label_1.grid   (row = 0, column = 1)
    label_2.grid   (row = 2, column = 1)
    vector_1.grid  (row = 1, column = 1)
    vector_2.grid  (row = 3, column = 1)
    submit.grid    (row = 5, column = 1)
    fillabel1.grid (row = 0, column = 0)
    fillabel2.grid (row = 0, column = 2)
    fillabel3.grid (row = 4, column = 0)
    fillabel4.grid (row = 6, column = 0)

    sp_window.mainloop()

# ######################################################################################################################
# ###DESIGN OF THE WINDOWS##############################################################################################
# ######################################################################################################################


# ###LINKED LIST WINDOW### #
def list_window_gen():
    # Definitions
    list_window = Tk()
    list_window['bg'] = "#363636"
    list_window.title("Lista")
    list_window.iconbitmap("icons/list_icon.ico")
    list_window.resizable(False, False)

    # FRAMES...........................................................................................................
    frame_crt  = Frame(list_window, bg = "#363636")
    frame_mplt = Frame(list_window, bg = "#363636")

    # WIDGETS.........................................................................................................

    # widgets of the window
    l_elements = Listbox(list_window, font = "Times 12", height = 20)

    # widgets of the creation frame
    label1     = Label(frame_crt, text = "Número de elementos:  ",
                     font = "Times 12", bg = "#363636", fg = "white")
    n_elements = Entry(frame_crt, font = "Times 12", width = 10)
    crtbtn     = Button(frame_crt, text = ("Gerar Lista"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: crt_list_queue(l_elements, n_elements.get(), 1, list_window))

    label2 = Label(list_window, text = ("Selecione um item da Lista    "),
                     font = "Times 12", bg = "#363636", fg = "white")

    infobtn = Button(frame_mplt, text = ("Informações do item"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: info_list((l_elements.get(ACTIVE)), list_window, l_elements))

    remvbtn = Button(frame_mplt, text = ("Remover o item da lista"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: rmv_list(l_elements, l_elements.get(ACTIVE), 0, (l_elements.size()-1),
                                                list_window))
    addbtn = Button(frame_mplt, text=("Adicionar item à lista"),
                    font="Times 12", bg="#363636", fg="white",
                    command=lambda: add_list_queue(l_elements, 1, 1, list_window))

    # labels used for spacing
    fil_label0 = Label(list_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label1 = Label(list_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label2 = Label(frame_crt,   bg = "#363636", font = "Times 12", width = 2)
    fil_label3 = Label(frame_mplt,  bg = "#363636", font = "Times 12", width = 2)
    fil_label4 = Label(list_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label5 = Label(frame_mplt,  bg = "#363636", font = "Times 12", width = 2)
    # INTERFACE...........................................................................................

    # frames
    frame_crt.grid  (row = 0, column = 1)
    frame_mplt.grid (row = 0, column = 5)
    # widgets
    l_elements.grid (row = 1, column = 1, sticky = "we")
    remvbtn.grid    (row = 1, column = 3, sticky = "we")
    infobtn.grid    (row = 0, column = 3, sticky = "we")
    addbtn.grid     (row = 2, column = 3, sticky = "we")
    label1.grid     (row = 0, column = 0)
    n_elements.grid (row = 0, column = 1)
    crtbtn.grid     (row = 0, column = 3)
    label2.grid     (row = 0, column = 3)

    # spacing labels
    fil_label0.grid (row = 0, column = 0)
    fil_label1.grid (row = 0, column = 2)
    fil_label2.grid (row = 0, column = 2)
    fil_label3.grid (row = 0, column = 2)
    fil_label4.grid (row = 0, column = 6)
    fil_label5.grid (row = 0, column = 4)

    fillabel = Label(list_window, font="Times 12", bg="#363636").grid(row=2, column=1)


    list_window.mainloop()


# ###STACK WINDOW### #
def stack_window_gen():
    # Definitions

    stack_window = Tk()
    stack_window['bg'] = "#363636"
    stack_window.title("Pilha")
    stack_window.iconbitmap("icons/stack_icon.ico")
    stack_window.resizable(False, False)

    # FRAMES...........................................................................................................
    frame_crt = Frame(stack_window, bg = "#363636")
    frame_mplt = Frame(stack_window, bg = "#363636")


    # WIDGETS.........................................................................................................

    # widgets of the window
    l_elements = Listbox(stack_window, font = "Times 12", height = 20)

    # widgets of the creation frame
    label1 = Label(frame_crt, text = "Número de elementos:  ",
                     font = "Times 12", bg = "#363636", fg = "white")
    n_elements = Entry(frame_crt, font = "Times 12", width = 10)
    crtbtn = Button(frame_crt, text = ("Gerar Pilha"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: crt_stack(l_elements, n_elements.get(), stack_window))

    label2 = Label(stack_window, text = ("Manipulação de itens da pilha    "),
                     font = "Times 12", bg = "#363636", fg = "white")

    infobtn = Button(frame_mplt, text = ("Peek (Visualizar o Topo) "),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: info_stack((l_elements.get(0)), stack_window, l_elements))

    remvbtn = Button(frame_mplt, text=("Pop (Remover o Topo)"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: rmv_stack(l_elements, 0, (l_elements.size()-1), stack_window))
    addbtn = Button(frame_mplt, text = ("Push (Adicionar ao topo)"),
                    font="Times 12", bg="#363636", fg="white",
                    command=lambda: add_stack(l_elements, 1, stack_window))

    # labels used for spacing
    fil_label0 = Label(stack_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label1 = Label(stack_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label2 = Label(frame_crt,    bg = "#363636", font = "Times 12", width = 2)
    fil_label3 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)
    fil_label4 = Label(stack_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label5 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)

    # INTERFACE...........................................................................................

    # frames
    frame_crt.grid  (row = 0, column = 1)
    frame_mplt.grid (row = 0, column = 5)
    # widgets
    l_elements.grid (row = 1, column = 1, sticky = "we")
    remvbtn.grid    (row = 1, column = 3, sticky = "we")
    infobtn.grid    (row = 0, column = 3, sticky = "we")
    addbtn.grid     (row = 2, column = 3, sticky = "we")
    label1.grid     (row = 0, column = 0)
    n_elements.grid (row = 0, column = 1)
    crtbtn.grid     (row = 0, column = 3)
    label2.grid     (row = 0, column = 3)

    # spacing labels
    fil_label0.grid (row = 0, column = 0)
    fil_label1.grid (row = 0, column = 2)
    fil_label2.grid (row = 0, column = 2)
    fil_label3.grid (row = 0, column = 2)
    fil_label4.grid (row = 0, column = 6)
    fil_label5.grid (row = 0, column = 4)

    fillabel = Label(stack_window, font = "Times 12", bg = "#363636").grid(row = 2, column = 1)

    # Advising about data structure integrity
    label_obs   = Label(stack_window, text = "OBS:Lembre-se do conceito de LIFO da pilha,\n "
                                             "respeitando assim sua integridade de dados",
                        font = "Times 12", bg = "#363636", fg = "white").grid(row = 2, column = 1)


    stack_window.mainloop()


# ###QUEUE WINDOW### #
def queue_window_gen():
    # Definitions
    queue_window = Tk()
    queue_window['bg'] = "#363636"
    queue_window.title("Fila")
    queue_window.iconbitmap("icons/queue_icon.ico")
    queue_window.resizable(False, False)

    # FRAMES...........................................................................................................
    frame_crt = Frame(queue_window, bg="#363636")
    frame_mplt = Frame(queue_window, bg="#363636")

    # WIDGETS.........................................................................................................

    # widgets of the window
    l_elements = Listbox(queue_window, font = "Times 12", height = 20)

    # widgets of the creation frame
    label1 = Label(frame_crt, text = "Número de elementos:  ",
                   font = "Times 12", bg = "#363636", fg = "white")
    n_elements = Entry(frame_crt, font = "Times 12", width = 10)
    crtbtn = Button(frame_crt, text = ("Gerar Fila"),
                    font = "Times 12", bg = "#363636", fg = "white",
                    command=lambda: crt_list_queue(l_elements, n_elements.get(), 2, queue_window))

    label2 = Label(queue_window, text = ("Manipulação de itens da fila    "),
                   font = "Times 12", bg = "#363636", fg = "white")

    infobtn = Button(frame_mplt, text = ("Cabeça da Fila"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command=lambda: info_queue(l_elements.get(0), queue_window, l_elements))

    remvbtn = Button(frame_mplt, text = ("Remover Cabeça"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: rmv_queue(l_elements, 0, (l_elements.size()-1), queue_window))
    addbtn = Button(frame_mplt, text=("Adicionar itens a fila"),
                    font="Times 12", bg="#363636", fg="white",
                    command=lambda: add_list_queue(l_elements, 1, 2, queue_window))

    # labels used for spacing
    fil_label0 = Label(queue_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label1 = Label(queue_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label2 = Label(frame_crt,    bg = "#363636", font = "Times 12", width = 2)
    fil_label3 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)
    fil_label4 = Label(queue_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label5 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)

    # INTERFACE...........................................................................................

    # frames
    frame_crt.grid  (row = 0, column = 1)
    frame_mplt.grid (row = 0, column = 5)
    # widgets
    l_elements.grid (row = 1, column = 1, sticky = "we")
    remvbtn.grid    (row = 1, column = 3, sticky = "we")
    infobtn.grid    (row = 0, column = 3, sticky = "we")
    addbtn.grid     (row = 2, column = 3, sticky = "we")
    label1.grid     (row = 0, column = 0)
    n_elements.grid (row = 0, column = 1)
    crtbtn.grid     (row = 0, column = 3)
    label2.grid     (row = 0, column = 3)

    # spacing labels
    fil_label0.grid (row = 0, column = 0)
    fil_label1.grid (row = 0, column = 2)
    fil_label2.grid (row = 0, column = 2)
    fil_label3.grid (row = 0, column = 2)
    fil_label4.grid (row = 0, column = 6)
    fil_label5.grid (row = 0, column = 4)

    fillabel = Label(queue_window, font = "Times 12", bg = "#363636").grid(row = 2, column = 1)


    label_obs = Label(queue_window, text = "OBS:Lembre-se do conceito de FIFO da fila,\n "
                                         "respeitando assim sua integridade de dados",
                      font = "Times 12", bg = "#363636", fg = "white").grid(row = 2, column = 1)

    queue_window.mainloop()


# ###TREE WINDOW### #
def tree_window_gen():
    # Definitions
    tree_window = Tk()
    tree_window['bg'] = "#363636"
    tree_window.title("Árvore Binária")
    tree_window.iconbitmap("icons/tree_icon.ico")
    tree_window.resizable(False, False)

    # FRAMES...........................................................................................................
    frame_crt = Frame(tree_window, bg="#363636")
    frame_mplt = Frame(tree_window, bg="#363636")
    frame_srch = Frame(frame_mplt, bg="#363636")

    # WIDGETS.........................................................................................................

    # widgets of the window
    l_elements = Listbox(tree_window, font = "Times 12", height = 20)

    # widgets of the creation frame
    label1 = Label(frame_crt, text = "Número de nós:  ",
                     font = "Times 12", bg = "#363636", fg = "white")
    n_elements = Entry(frame_crt, font = "Times 12", width = 10)
    crtbtn = Button(frame_crt, text = ("Gerar Árvore Binária"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: crt_tree(l_elements, n_elements.get(), tree_window))

    label2 = Label(tree_window, text = ("Selecione um nó da Árvore    "),
                     font = "Times 12", bg = "#363636", fg = "white")

    infobtn = Button(frame_mplt, text = ("Informações do nó"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: info_tree((l_elements.get(ACTIVE)), tree_window, n_elements.get(),
                                                 l_elements))

    remvbtn = Button(frame_mplt, text = ("Remover o nó"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: rmv_tree(l_elements, l_elements.get(ACTIVE), tree_window))

    addbtn = Button(frame_mplt, text=("Adicionar nó a Árvore"),
                    font="Times 12", bg="#363636", fg="white",
                    command=lambda: add_tree(l_elements, 1, tree_window))

    srtbtn1 = Button(frame_mplt, text = ("Sort League_ID"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: srt_tree(l_elements, "league_id", tree_window))

    srtbtn2 = Button(frame_mplt, text = ("Sort Match_Api_ID"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: srt_tree(l_elements, "match_api_id", tree_window))

    srchbtn = Button(frame_srch, text = "Search",
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: search(s_elements.get(), l_elements, tree_window))

    drawbtn = Button(tree_window, text = "Desenhar", font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: define_t(arvore.root, 120))

    s_elements = Entry(frame_srch, font = "Times 12", width = 10)

    # labels used to control spacing
    fil_label0 = Label(tree_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label1 = Label(tree_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label2 = Label(frame_crt,   bg = "#363636", font = "Times 12", width = 2)
    fil_label3 = Label(frame_mplt,  bg = "#363636", font = "Times 12", width = 2)
    fil_label4 = Label(tree_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label5 = Label(frame_mplt,  bg = "#363636", font = "Times 12", width = 2)
    fil_label6 = Label(frame_mplt,  bg = "#363636", font = "Times 12", width = 2)

    # INTERFACE...........................................................................................

    # frames
    frame_crt.grid  (row = 0, column = 1)
    frame_mplt.grid (row = 0, column = 5)
    frame_srch.grid (row = 2, column = 7)
    # widgets
    l_elements.grid (row = 1, column = 1, sticky = "we")
    remvbtn.grid    (row = 1, column = 3, sticky = "we")
    infobtn.grid    (row = 0, column = 3, sticky = "we")
    addbtn.grid     (row = 2, column = 3, sticky = "we")
    srtbtn1.grid    (row = 0, column = 7, sticky = "we")
    srtbtn2.grid    (row = 1, column = 7, sticky = "we")
    s_elements.grid (row = 0, column = 0)
    srchbtn.grid    (row = 0, column = 1)
    label1.grid     (row = 0, column = 0)
    n_elements.grid (row = 0, column = 1)
    crtbtn.grid     (row = 0, column = 3)
    label2.grid     (row = 0, column = 3)
    drawbtn.grid    (row = 0, column = 8, padx = 20)

    # spacing labels
    fil_label0.grid (row = 0, column = 0)
    fil_label1.grid (row = 0, column = 2)
    fil_label2.grid (row = 0, column = 2)
    fil_label3.grid (row = 0, column = 2)
    fil_label4.grid (row = 0, column = 6)
    fil_label5.grid (row = 0, column = 4)
    fil_label6.grid (row = 0, column = 6)

    fillabel = Label(tree_window, font = "Times 12", bg = "#363636").grid(row = 2, column = 1)

    tree_window.mainloop()


# ###GRAPH WINDOW### #
def graph_window_gen():
    # Definitions
    graph_window = Tk()
    graph_window['bg'] = "#363636"
    graph_window.title("Grafo")
    graph_window.iconbitmap("icons/graph_icon.ico")
    graph_window.resizable(False, False)

    # FRAMES...........................................................................................................
    frame_crt  = Frame(graph_window, bg = "#363636")
    frame_mplt = Frame(graph_window, bg = "#363636")
    frame_srch = Frame(frame_mplt,   bg = "#363636")

    # WIDGETS.........................................................................................................
    global grafo

    # widgets of the window
    l_elements = Listbox(graph_window, font = "Times 12", height = 20)

    # widgets of the creation frame
    label1 = Label(frame_crt, text = "Número de vetores:  ",
                     font = "Times 12", bg = "#363636", fg = "white")
    n_elements = Entry(frame_crt, font = "Times 12", width = 10)
    crtbtn = Button(frame_crt, text = ("Gerar Grafo"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: crt_graph(l_elements, n_elements.get(), graph_window))

    label2 = Label(graph_window, text = ("Selecione um vetor do Grafo    "),
                     font = "Times 12", bg = "#363636", fg = "white")

    infobtn = Button(frame_mplt, text = ("Informações do vetor"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: info_graph((l_elements.get(ACTIVE)), graph_window, l_elements))

    remvbtn = Button(frame_mplt, text = ("Menor distância"),
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: shortest_dist(l_elements))

    addbtn = Button(frame_mplt, text=("Adicionar vetor ao grafo"),
                    font="Times 12", bg="#363636", fg="white",
                    command=lambda: add_graph(l_elements, 1, graph_window))

    srchbtn = Button(frame_srch, text = "Search",
                     font = "Times 12", bg = "#363636", fg = "white",
                     command = lambda: search(s_elements.get(), l_elements, graph_window))

    s_elements = Entry(frame_srch, font = "Times 12", width = 10)

    # labels used for spacing
    fil_label0 = Label(graph_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label1 = Label(graph_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label2 = Label(frame_crt,    bg = "#363636", font = "Times 12", width = 2)
    fil_label3 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)
    fil_label4 = Label(graph_window, bg = "#363636", font = "Times 12", width = 2)
    fil_label5 = Label(frame_mplt,   bg = "#363636", font = "Times 12", width = 2)

    # INTERFACE...........................................................................................

    # frames
    frame_crt.grid  (row = 0, column = 1)
    frame_mplt.grid (row = 0, column = 5)
    frame_srch.grid (row = 0, column = 5)
    # widgets
    l_elements.grid (row = 1, column = 1, sticky = "we")
    remvbtn.grid    (row = 1, column = 3, sticky = "we")
    infobtn.grid    (row = 0, column = 3, sticky = "we")
    addbtn.grid     (row = 2, column = 3, sticky = "we")
    s_elements.grid (row = 0, column = 0)
    srchbtn.grid    (row = 0, column = 1)
    label1.grid     (row = 0, column = 0)
    n_elements.grid (row = 0, column = 1)
    crtbtn.grid     (row = 0, column = 3)
    label2.grid     (row = 0, column = 3)

    # labels for spacing
    fil_label0.grid (row = 0, column = 0)
    fil_label1.grid (row = 0, column = 2)
    fil_label2.grid (row = 0, column = 2)
    fil_label3.grid (row = 0, column = 2)
    fil_label4.grid (row = 0, column = 6)
    fil_label5.grid (row = 0, column = 4)

    fillabel = Label(graph_window, font = "Times 12", bg = "#363636").grid(row = 2, column = 1)

    graph_window.mainloop()


# ###ABOUT WINDOW### #
def about():
    # ABOUT WINDOW DEFINITIONS
    about_window = Tk()
    about_window.title("Sobre o Projeto")
    about_window.iconbitmap("icons/about_icon.ico")
    about_window['bg'] = "#363636"
    about_window.resizable(False, False)

    # Label with the developers team message for the users
    label_info_br = Label(about_window, font = "Times 12", bg = "#363636", fg = "white", justify = LEFT,
                          wraplength = 300, bd = 5, relief = "raised",
                          text = "     Essa aplicação refere-se a um projeto da disciplina estrutura de dados "
                                 "ministrada pelo professor Alan Pedro da Silva.\n     Esse projeto propõe a "
                                 "manipulação das estruturas: lista encadeada, fila, pilha, árvore binária e grafo. "
                                 "Caso deseje saber mais, seja sobre o projeto ou sobre as estruturas, acesse:\n\n"
                                 " https://github.com/zadhart/EstruturaDeDados"
                                 "\n\nGRUPO:\nJoão Vitor Santos Tavares\nRafael Emílio Lima Alves"
                                 "\nRick Martim Lino dos Santos\nWagner Anthony de Medeiros Silva\n")

    label_info_br.pack()

    about_window.mainloop()


# ###MAIN WINDOW### #
def main():
    # MAIN'S WINDOW DEFINITIONS
    initial_window = Tk()
    initial_window.title("Projeto Final Estrutura de Dados")
    initial_window.iconbitmap("icons/main_icon.ico")
    initial_window['bg'] = '#363636'
    initial_window.resizable(False, False)

    # MAIN'S WINDOW BUTTONS

    # List button
    btn1 = Button(initial_window, text = 'Lista Encadeada', command = lambda: list_window_gen(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # Stack button
    btn2 = Button(initial_window, text = 'Pilha',           command = lambda: stack_window_gen(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # Queue button
    btn3 = Button(initial_window, text = 'Fila',            command = lambda: queue_window_gen(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # Tree button
    btn4 = Button(initial_window, text = 'Árvore Binária',  command = lambda: tree_window_gen(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # Graph button
    btn5 = Button(initial_window, text = 'Grafo',           command = lambda: graph_window_gen(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # About button
    btn6 = Button(initial_window, text='Sobre o Projeto (?)',         command = lambda: about(),
                      bg = "#363636", fg = "white", font = "Times 20", bd = 5, width = 20, height = 1)

    # MAIN'S WINDOWS GRIDS

    btn1.grid(row = 0, column = 3)
    btn2.grid(row = 1, column = 3)
    btn3.grid(row = 2, column = 3)
    btn4.grid(row = 3, column = 3)
    btn5.grid(row = 4, column = 3)
    btn6.grid(row = 5, column = 3)

    initial_window.mainloop()


main()  # calling of the main function
