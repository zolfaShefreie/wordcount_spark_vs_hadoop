

stopwords = ['significantly', 'wasn', 'bottom', 'higher', 'won', 'cs', 'fully', 'points', 'msie', 'ourselves', 'nor',
             'thorough', 'upon', 'up', 'minus', 'tv', 'case', 'respectively', 'thanks', 'second', 'many', 'out', 'finds',
             'becoming', 'ru', 'gh', 'group', 'likely', 'anymore', 'mr', 'seventy', 'oldest', 'information', 'therell',
             'herein', 'most', 'aren', 'substantially', "hadn't", "'twas", 'having', 'associated', "that's", 'noted',
             'ninety', 'mq', 'pa', 'ws', 'known', 'thirty', 'regarding', 'gotten', 'especially', 'okay', 'which',
             "how'll", 'theyve', 'available', "i've", 'youre', 'arent', 'somebody', 'what', "you've", 'maynt', 'herse”',
             'namely', 'look', 'text', 'pl', 'nu', 'without', 'maybe', 'beginnings', "mayn't", 'br', 'problem', 'once',
             'shes', "'ve", 'htm', 'neither', 'thoroughly', 'used', 'au', 'described', 'eh', 'anyway', "he'd", 'ph',
             'je', 'mm', 'index', 'fifth', 'third', 'tr', 'specified', "how's", 'really', 'do', 'goes', 'forty', 'http',
             'ref', 'gm', 'about', 'shown', "it'll", 'better', "you'll", 'another', 'ex', 'um', 'affected', 'cy', 'comes',
             'werent', 'getting', 'soon', 'meanwhile', 'currently', 'alone', "mightn't", 'al', 'bh', 'om', 'possibly',
             'neverless', 'pp', 'over', 'mean', 'thou', "you'd", 'instead', 'nothing', 'changes', 'eight', 'tries',
             "'tis", 'whereby', 'stop', "why's", 'homepage', 'itll', 'beside', 'him', 'ar', 'interests', 'gmt', 'parted',
             "they'd", 'seems', 'tip', 'self', "don't", 'nay', 'wonder', 'appreciate', 'til', 'brief', 'announce',
             'various', 'wells', 'cd', 'o', 'inside', 'a', "t's", 'resulted', 'isn', 'wasnt', 'newer', 'toward',
             'pointed', 'tends', 'by', 'ly', 'although', 'clearly', "what's", 'copy', "one's", 'aw', 'following',
             'happens', 'could', 'good', 'net', 'vn', "ain't", "what'd", 'mine', 'latest', 'work', 'ro', 'useful',
             'round', 'evermore', 'ye', 'unlike', 'whichever', 'numbers', 'wouldnt', 'necessarily', 'ht', 'keep', 'li',
             'problems', 'thereve', 'similarly', 'while', 'find', "what'll", 'showing', 'tried', 'presenting', 'amidst',
             'said', 'vs', 'poorly', 'cases', 'html', 'kn', 'keeps', 'differ', 'areas', 'mightnt', 'grouped', 'other',
             'have', 'side', 'somehow', 'website', 'provides', 'nc', 'know', "she'll", 'mg', 'taking', 'nine', 'room',
             'it', 'er', 'highest', 'pt', 'fo', 'uk', 'did', 'y', 'therere', 'sec', 'against', 'latter', 'vi',
             'definitely', 'za', 'gone', 'que', 'giving', 'come', 'ii', 'beforehand', 'example', 'forth', 'formerly',
             'added', 'can', 'ky', 'eleven', 'onto', 'cf', 'though', 'among', 'web', "she'd", 'll', 'longest', 'auth',
             'predominantly', 'caption', 'webpage', 'who', 'et', 'bs', 'ignored', 'seeming', 'v', 'con', 'hk', 'org',
             'sometime', 'ed', 'tj', 'c', 'sy', 'uy', 'ours', 'whod', 'un', 'seem', 'abst', 'world', 'whos', "wouldn't",
             'or', 'largely', 'click', 'rooms', "weren't", 'to', 'latterly', 'does', 'wed', 'ts', "isn't", 'almost',
             'lu', 'null', 'cry', 'sometimes', 'member', 'wherever', 'i.e.', 'its', "who'd", 'lets', 'l', 'secondly',
             'had', 'dj', 'awfully', "would've", 'younger', "that'll", 'your', 'looks', 'readily', 'suggest',
             'elsewhere', 'towards', 'ae', 'youd', 'amongst', 'directly', 'tt', 'shows', 'seven', 'recent', 'consider',
             'nl', 'ls', 'new', 'x', 'top', 'faces', 'vols', 'otherwise', 'himse”', 'plus', 'man', 'except', 'newest',
             'pm', 'mostly', 'end', 'five', 'are', "can't", "there're", 'jp', 'regards', 'outside', 'for', 'going',
             'keys', 'date', 'tz', 'the', 'downs', 'face', 'smaller', 'system', 'than', 'above', 'today', 'aq', 'those',
             'mz', 'she', 'yourself', 'cmon', 'someone', 'gp', 'mil', 'sr', 'gb', 'men', 'containing', 'affects',
             'seemed', 'wholl', 'years', 'accordance', 'certainly', 'wish', 'ge', 'we', "c'mon", 'these', 'hadnt',
             "needn't", 'sorry', 'whomever', 'apparently', 'need', 'every', 'welcome', 'put', 'mug', 'he', 'course',
             'her', 'yours', 'hello', 'backing', 'cg', 'gets', 'greatest', "they're", 'com', 'ie', 'heres', 'nf',
             'considering', 'cr', 'va', 'ne', 'working', 'dare', "he'll", 'wanted', 'into', 'thatll', "they've",
             'whereupon', 'viz', 'on', 'usefulness', "who's", 'zr', 'ended', "must've", 'don', 'around', 'm',
             'obviously', 'gg', 'mv', 'their', 'ai', 'together', 'ltd', 'fire', 'several', 'wont', 'all', 'il', "let's",
             'being', 'hereby', 'presumably', 'mn', 'perhaps', 'co.', 'still', 'gn', 'ao', 'immediately', 'kp', 'gt',
             'down', 'adj', 'whim', 'affecting', 'present', 'nowhere', 'specify', 'mk', 'rw', 'buy', 'cm', 'act', 'cant',
             'normally', 'tn', 'az', 'shed', 'undoing', "aren't", 'would', 'nr', 'bt', 'worked', 'not', 'bb', 'saying',
             'invention', "daren't", 'number', 'using', 'insofar', 'bo', 'im', 'particularly', 'uses', 'likewise',
             'needs', "i'd", 'yt', 'na', 'dear', 'of', 'whatll', 've', 'wherein', 'taken', 'mustnt', 'hell', 'free',
             'few', 'from', 'appropriate', 'immediate', 'ad', 'aside', 'weren', 'thered', 'before', 'must', 'ending',
             'resulting', 'sides', 'also', 'places', 'might', 'downwards', 'sj', 'ill', 'fify', 'de', 'fifty',
             'whereafter', 'due', 'fewer', 'again', 'provided', 'show', 'pk', 'sc', 'that', "there'll", "you're",
             'accordingly', 'asks', 'run', 'young', 'inner', 'call', 'dm', 'let', 'specifically', 'am', 'id', 'cv',
             'low', 'yourselves', 'thousand', 'thought', 'hu', 'members', 'la', 'amount', 'there', 'saw', 'trying',
             'primarily', 'followed', "there've", 'kept', 'later', 'thing', 'ways', 'importance', 'contains', 't',
             'asking', 'neednt', 'zero', 'underneath', 'forward', 'pr', 'cz', 'enough', 'oh', 'thin', 'selves', 'gives',
             'shant', 'important', 'refs', "hasn't", "when'll", 'here', 'but', 'sup', 'gi', 'right', 'asked', "c's",
             'back', 'more', 'rd', 'ord', 'shall', "oughtn't", 'www', 'tw', "why'd", 'myself', 'hm', 'hr', "when'd",
             'pages', 'differently', 'interest', 'r', 'through', "where's", 'proud', 'follows', 'move', "where'd",
             'no-one', 'fx', 'mh', 'usefully', 'omitted', 'sincere', 'bg', 'backed', 'two', 'computer', 'ones', 'e',
             'make', 'sa', 'ahead', "a's", 'ableabout', 'making', 'ch', 'sg', "couldn't", 'bv', 'only', "shouldn't",
             'biol', 'hn', 'iq', 'any', 'w', 'opening', 'fj', "could've", 'made', 'downing', 'became', 'join', 'each',
             'turn', 'hither', 'length', 'fr', 'took', 'novel', 'unto', 'at', 'got', 'downed', 'bill', 'theres', 'bm',
             'necessary', 'fm', 'needing', 'sl', 'potentially', 'groups', 'noone', "why'll", 'uz', 'nobody', 'i',
             'looking', 'whither', 'besides', 'aint', 'placed', 'thanx', 'bw', 'very', 'tell', 'them', 'line', 'width',
             'cx', 'specifying', 'were', 'pg', 'been', 'see', 'effect', 'strongly', 'anyhow', 'bi', 'kz', 'cl', 'twenty',
             'hi', 'sensible', 'you', 'evenly', 'big', 'ask', 'between', 'help', 'thinks', 'everywhere', 'means', 'words',
             'nevertheless', 'haven', 'rather', 'state', 'across', 'first', 'home', 'former', 'is', 'puts', 'along',
             'non', 'reasonably', 'say', 'seeing', 'mu', 'six', 'older', 'serious', 'corresponding', 'way', 'sure',
             'give', "here's", 'nearly', 'somethan', 'whom', "i'm", 'empty', 'came', 'shouldn', 'particular', 'myse”',
             'wants', 'trillion', 'use', 'related', 'results', 'bd', 'anybody', 'next', 'sm', 'small', "'ll", 'think',
             'greater', "might've", 'contain', 'briefly', 'inc.', 'yet', 'such', 'cause', 'quickly', 'area', 'gu',
             'lower', 'ma', 'throughout', 'everything', 'su', 'interesting', 'anywhere', 'allow', 'sb', 'during',
             'smallest', 'kh', 'ca', 'ga', 'little', 'unfortunately', 'yes', 'yu', 'ba', 'si', 'makes', 'seen', 'within',
             'ke', 'so', 'thoughh', 'unless', 'u', 'bn', 'want', 'less', 'then', 'whether', 'under', 'despite', 'now',
             'couldn', 'mainly', 'tc', 'gq', 'both', 'get', "he's", 'reserved', 'fill', 'high', 'havent', 'unlikely',
             'just', "what've", 'indeed', 'whatever', 'gw', 'regardless', 'ni', 'se', 'found', 'pn', "should've",
             'twice', 'given', 'often', 'hardly', 'km', 'own', 'gave', 'million', 'kg', 'with', 'detail', 'via', 'clear',
             'vu', 'ive', 'abroad', 'order', 'oughtnt', 'relatively', 'dk', 'howbeit', 'parts', 'backwards', 'hers',
             'gov', 'too', 'vol', 'mt', 'theyre', 'wf', 'ought', 'wouldn', 'gs', 'opened', 'sees', 'shell', 'place', 'd',
             "shan't", 'past', 'lb', 'ec', 'goods', "who'll", 'lv', 'whatve', 'three', "we're", 'didnt', 'thereof', 'our',
             'should', 'therein', 'research', 'ordered', 'whole', 'anyways', 'never', 'mrs', 'edu', 'furthering', 'tis',
             'obtain', 'because', 'didn', 'consequently', 'tk', 'hereupon', 'sent', 'however', 'lt', 'whereas', 's',
             'early', 'p', 'either', 'dz', 'tg', 'mc', 'cn', 'no', 'when', 'td', 'pointing', 'sk', 'me', 'inc', 'ends',
             'versus', 'point', 'thatve', 'apart', 'my', 'indicate', 'orders', 'inward', 'whose', 'themselves', 'whence',
             'half', 'itself', 'usually', 'k', 'tp', 'slightly', 'owing', 'presented', 'even', 'netscape', 'until',
             'obtained', 'hopefully', 'whenever', 'truly', 'twas', 'nonetheless', 'hundred', 'vc', 'darent', 'four',
             'best', "wasn't", 'turned', 'near', "it's", "didn't", "when's", 'value', 'eg', 'facts', 'mx', 'appear',
             'thereafter', 'one', 'io', 'bj', 'widely', 'hasnt', 'tf', 'afterwards', 'great', 'wanting', 'theirs',
             'page', 'furthermore', 'longer', 'go', 'probably', 'greetings', 'gy', 'like', 'farther', 'somewhere',
             'went', '10', 'after', 'describe', 'nz', 'kind', 'ua', 'etc', 'allows', 'md', 'f', 'why', 'mp', 'turning',
             'willing', 'this', 'doing', 'ago', 'in', 'ups', 'always', "how'd", 'an', 'sd', 'full', 'anyone', 'b', 'sz',
             'previously', 'fi', 'ck', "there'd", 'ng', 'hid', 'showed', 'far', 'take', 'states', 'his', 'thank', 'h',
             'interested', 'generally', 'approximately', 'alongside', 'st', 'ki', 'ms', 'ff', 'cannot', 'where',
             'similar', 'itd', 'certain', 'seconds', 'someday', 're', 'sub', 'entirely', 'whoever', 'pe', 'herself',
             "where'll", 'none', 'exactly', 'dont', 'n', 'liked', 'forever', 'lc', 'ug', "they'll", 'ever', 'well',
             'presents', 'general', 'year', 'bf', 'possible', "doesn't", 'thats', 'theyd', 'youngest', 'fairly',
             'beginning', 'has', 'furthers', 'qa', '39', 'microsoft', 'last', 'long', 'miss', 'hasn', 'further', 'till',
             'become', 'indicated', 'actually', 'able', 'sixty', 'billion', 'hereafter', 'z', 'twelve', 'believe',
             'quite', 'everybody', 'seriously', 'same', 'hes', 'youve', 'jo', 'shouldnt', 'will', 'zm', 'they', 'eighty',
             'sufficiently', 'sn', 'tm', "mustn't", 'front', 'causes', 'py', 'gd', 'becomes', 'how', 'according',
             'concerning', 'hed', 'parting', 'pf', 'overall', 'us', 'per', 'needed', 'thence', 'merely', "i'll",
             'theyll', 'doubtful', 'ag', 'off', 'qv', 'thereupon', 'part', 'therefore', 'hence', 'backward', 'youll',
             'begins', 'was', 'already', 'opposite', 'try', 'name', 'lest', 'notwithstanding', 'upwards', 'jm', 'ah',
             'meantime', 'mw', 'lr', 'ir', 'opens', 'j', "we'll", 'showns', "haven't", 'fifteen', 'thereto', 'much',
             'moreover', 'site', 'wheres', 'knows', 'cc', 'began', 'somewhat', 'cu', 'felt', 'weve', 'af', 'et-al', 'be',
             "there's", 'beyond', 'int', 'behind', 'gf', "we'd", 'g', 'gr', 'q', 'anything', 'ci', 'lately', 'np', 'th',
             'away', 'ee', 'please', 'indicates', 'whilst', 'significant', 'section', 'ml', 'may', "we've", 'arpa',
             "she's", 'done', 'himself', 'promptly', 'successfully', 'pmid', 'kw', 'ok', 'doesn', 'thereby', 'open',
             'least', 'uucp', "won't", 'others', 'works', 'since', 'nos', 'turns', 'thick', 'doesnt', "that've", 'gl',
             'lk', 'begin', 'old', 'some', 'ran', "it'd", 'furthered', 'mo', 'inasmuch', 'fact', 'ordering', 'vg', 'fk',
             'arise', 'else', 'neverf', 'thru', 'es', 'everyone', 'fix', 'ring', 'grouping', 'kr', 'ten', 'sv', 'adopted',
             'something', 'thoughts', 'knew', 'couldnt', 'as', 'co', 'isnt', 'throug', 'large', 'amid', 'nd', 'and',
             'different', 'recently', 'backs', 'pw', 'says', 'bz', 'itse”', 'mill', 'test', 'whats', 'if', 'sh',
             'things', 'below', 'thus', 'beings', 'amoungst', 'u']