import base64
import uuid
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))

    if chart_type == '#1':
        do_bar_chart_action(data, **kwargs)

    elif chart_type == '#2':
        do_pie_chart_action(data, **kwargs)

    elif chart_type == '#3':
        do_line_chart_action(data, **kwargs)

    else:
        print('Failed to identify chart type...')

    plt.tight_layout()

    chart = get_graph()
    return chart


def do_bar_chart_action(data, **kwargs):
    print('bar chart')
    #plt.bar(data['transaction_id'], data['price'])
    sns.barplot(x='transaction_id', y='price', data=data)


def do_pie_chart_action(data, **kwargs):
    labels = kwargs.get('labels')
    plt.pie(data=data, x='price', labels=labels)


def do_line_chart_action(data, **kwargs):
    plt.plot(data['transaction_id'], data['price'], color='green', marker='o')
    print('line chart')

