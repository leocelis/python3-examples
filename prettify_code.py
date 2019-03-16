import ujson

from pygments import highlight, lexers, formatters

d = {'meta': [('name', 'keywords'), ('content',
                                     'Walt Disney Company (The) tiempo real, Walt Disney Company (The) tiempo real, DIS tiempo-real, DIS tiempo real, cotización de valores en tiempo real DIS, DIS cotización en streaming')],
     'tbody': [], 'noscript': [],
     'select': [('style', 'display: none'), ('id', 'quotepage'), ('onchange', 'CheckInput()')],
     'style': [('type', 'text/css')], 'tr': [], 'h4': [], 'title': [],
     'span': [('id', 'quotes_content_left__NOCPAndDate')], 'br': [], 'b': [],
     'img': [('src', 'http://nasdaq.122.2O7.net/b/ss/nasdaqprod/1/H.1--NS/0'), ('height', '1'), ('width', '1'),
             ('border', '0'), ('alt', '')], 'li': [],
     'html': [('lang', 'en-us'), ('class', 'wide translated-quotes  no-js'), ('xmlns:og', 'http://ogp.me/ns#'),
              ('xmlns:fb', 'https://www.facebook.com/2008/fbml')], 'label': [('for', 'cookiepref')],
     'ul': [('class', 'inline noindent')], 'header': [('id', 'global_header')], 'thead': [], 'h1': [],
     'option': [('value', 'chartingfunds')], 'p': [],
     'script': [('type', 'text/javascript'), ('src', 'http://www.nasdaq.com/includes/foresee/foresee-trigger.js')],
     'th': [], 'body': [('id', 'body')], 'td': [], 'table': [('class', 'backdrop'), ('id', 'backdrop')],
     'link': [('rel', 'stylesheet'), ('type', 'text/css'), ('href', '/includes/global-translated.min-11292017v1.css')],
     'head': [],
     'form': [('name', 'quotenav'), ('id', 'quotenav'), ('method', 'get'), ('onsubmit', 'return CheckInput()')],
     'iframe': [('id', 'msymbollookupframe'), ('frameborder', '0'),
                ('style', 'width: 350px; height: 350px; margin-left: 25px; visibility: visible;')],
     'input': [('name', 'ctl00$ICU$refreshbutton'), ('type', 'button'), ('id', 'ICU_refreshbutton'),
               ('onclick', 'refresh()'), ('value', 'Actualiz')], 'textarea': [('onkeypress',
                                                                               "if(event.keyCode ==13){nasdaqIndexRow.myListGo()}else if(event.keyCode == 27){$('.close').click();}"),
                                                                              ('id', 'myListInput'),
                                                                              ('name', 'myListInput'), ('cols', '35'),
                                                                              ('rows', '3'), ('class', 'fontS14px')],
     'small': [], 'h3': [],
     'a': [('href', 'javascript:void(0)'), ('class', 'red-button'), ('onclick', 'nasdaqIndexRow.clearMyList();')],
     'h2': [('style', 'text-align:center;')], 'button': [('type', 'submit'), ('id', 'stock-search-submit')],
     'div': [('class', 'clearB')]}

formatted_json = ujson.dumps(d, sort_keys=True, indent=4)
colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
print(colorful_json)
