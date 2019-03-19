from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from concurrent.futures import ThreadPoolExecutor
import time
import sys


def publish():
    wp = Client(
        'http://192.168.39.75:30223/xmlrpc.php',
        'repo',
        'P6^)DbGN5XI8f6R)qa')
    start = time.perf_counter_ns()
    print(wp.call(GetPosts()))
    end = time.perf_counter_ns()
    print('Query  time (ms)', (end - start) / 10.0**6)

    post = WordPressPost()
    post.title = 'My new title'
    post.content = 'This is the body of my new post. With new comment'
    post.terms_names = {
        'post_tag': ['test', 'firstpost'],
        'category': ['Introductions', 'Tests']
    }
    post.post_status = 'publish'
    start = time.perf_counter_ns()
    wp.call(NewPost(post))
    end = time.perf_counter_ns()
    print('Insert time (ms)', (end - start) / 10.0**6)


if __name__ == '__main__':
    try:
        workers, requests = (int(x) for x in sys.argv[1:])
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for x in range(requests):
                executor.submit(publish)
    except ValueError:
        print('Usage: python publisher.py <workers:int> <requests:int>')
