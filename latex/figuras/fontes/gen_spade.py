"""Gera figuras/spade-modelo-agente.svg: modelo de agente do SPADE 4.1.4 e caminho de uma mensagem.
Elaborado com base na documentação oficial do SPADE (páginas The SPADE Agent Model, Quick Start e
Presence Notification). Uso: python3 gen_spade.py; depois
  rsvg-convert -f pdf ../spade-modelo-agente.svg -o ../spade-modelo-agente.pdf"""
import os
W,H=1000,580
F='Liberation Sans, Arial, Helvetica, sans-serif'
INK='#1a1a1a'; AG='#e3e9f2'; SV='#f2f2f2'
out=[]
def rect(x,y,w,h,fill='#ffffff',sw=1.6,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{d}/>')
def text(x,y,s,size=16,bold=False,anchor='middle',italic=False):
    b=' font-weight="bold"' if bold else ''
    it=' font-style="italic"' if italic else ''
    out.append(f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" text-anchor="{anchor}" fill="{INK}"{b}{it}>{s}</text>')
def arrow(pts,label=None,lx=None,ly=None):
    d=' '.join(('M' if i==0 else 'L')+f'{x} {y}' for i,(x,y) in enumerate(pts))
    out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8" marker-end="url(#arr)"/>')
    if label:
        w=len(label)*8.4+12
        out.append(f'<rect x="{lx-w/2}" y="{ly-15}" width="{w}" height="21" fill="#ffffff"/>')
        text(lx,ly+1,label,size=15)
def agent(x0,title,jid):
    w=370
    rect(x0,10,w,560,fill=AG,sw=2.2)
    text(x0+w/2,40,title,size=19,bold=True)
    text(x0+w/2,62,jid,size=15,italic=True)
    rect(x0+15,76,w-30,214)
    text(x0+w/2,97,'Comportamentos',size=17,bold=True)
    text(x0+w/2,117,'cíclico, periódico, execução única,',size=15)
    text(x0+w/2,136,'tempo limite, máquina de estados finitos',size=15)
    for i,bxx in enumerate([x0+30,x0+195]):
        rect(bxx,148,145,130)
        text(bxx+72,170,f'Comportamento {i+1}',size=15,bold=True)
        rect(bxx+12,178,121,38,dash='6 4'); text(bxx+72,203,'modelo',size=15)
        rect(bxx+12,226,121,38); text(bxx+72,251,'fila',size=15)
    rect(x0+15,330,w-30,64)
    text(x0+w/2,358,'Despachante de mensagens',size=17,bold=True)
    text(x0+w/2,380,'usa os modelos para escolher a fila',size=15)
    rect(x0+15,420,w-30,64)
    text(x0+w/2,448,'Conexão com a plataforma',size=17,bold=True)
    text(x0+w/2,470,'JID e senha, fluxo XMPP persistente',size=15)
    rect(x0+15,500,(w-40)/2,54); text(x0+15+(w-40)/4,524,'Presença',size=15,bold=True); text(x0+15+(w-40)/4,544,'contatos',size=15)
    x2=x0+25+(w-40)/2
    rect(x2,500,(w-40)/2,54); text(x2+(w-40)/4,524,'Interface web',size=15,bold=True); text(x2+(w-40)/4,544,'monitoramento',size=15)
    return x0,w
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
out.append(f'<defs><marker id="arr" markerWidth="13" markerHeight="11" refX="11" refY="5.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L11 5.5 L1 10" fill="none" stroke="{INK}" stroke-width="1.6"/></marker></defs>')
out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
ax,aw=agent(10,'Agente A','agente-a@dominio')
bx,bw=agent(620,'Agente B','agente-b@dominio')
rect(400,300,200,200,fill=SV,sw=2.2)
text(500,330,'Servidor XMPP',size=18,bold=True)
text(500,358,'registro e',size=15); text(500,378,'autenticação',size=15)
text(500,402,'encaminhamento',size=15)
text(500,426,'presença',size=15)
text(500,458,'dedicado (Prosody)',size=15,italic=True)
text(500,478,'ou embutido',size=15,italic=True)
arrow([(ax+102,278),(ax+102,330)],label='envio',lx=ax+102,ly=313)
arrow([(ax+102,394),(ax+102,420)])
arrow([(ax+aw-15,452),(400,452)])
arrow([(600,452),(bx+15,452)])
arrow([(bx+102,420),(bx+102,394)])
arrow([(bx+102,330),(bx+102,278)],label='entrega',lx=bx+102,ly=313)
out.append('</svg>')
here=os.path.dirname(os.path.abspath(__file__))
p=os.path.join(here,'..','spade-modelo-agente.svg')
open(p,'w',encoding='utf-8').write('\n'.join(out)); print(p)
