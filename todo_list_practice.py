from fasthtml import common as fh # type: ignore

def render(todo):
    tid = f'todo-{todo.id}'
    toggle = fh.A('Toggle ', hx_get=f'/toggle/{todo.id}', target_id=tid)  # noqa: F841
    delete = fh.A('Delete ', hx_delete=f'{todo.id}',
                  hx_swap='outerHTML', target_id=tid, )  # noqa: F841
    return fh.Li(toggle, delete,
                 todo.title + (' ✅' if todo.done else ''),
                 id=tid)  # type: ignore # noqa: F821

app,rt,todos,Todo = fh.c('todos.db', live=True, render=render,
                                       id=int, title=str, done=bool, pk='id')

def mk_input(): return fh.Input(placeholder='Add Todo', 
                                id='title', hx_swap_oob='true')

@rt('/')
def get():
    frm = fh.Form(fh.Group(mk_input(), 
                           fh.Button("Add")),
                  hx_post='/', target_id='todo-list', hx_swap='beforeend')
    return fh.Titled('Todos', 
                     fh.Card(
                     fh.Ul(*todos(), id='todo-list'), 
                     header=frm)
                     )

@rt('/')
def post(todo:Todo): return todos.insert(todo), mk_input() # type: ignore


@rt('/{tid}')
def delete(tid:int): todos.delete(tid)

@rt('/toggle/{tid}')
def get(tid:int):  # noqa: F811
    todo = todos[tid]
    todo.done = not todo.done
    return todos.update(todo)

fh.serve()