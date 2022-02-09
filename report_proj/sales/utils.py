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


def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))

    key = get_key(results_by)
    grouped_data = data.groupby(key, as_index=False)['total_price'].agg('sum')
    print(grouped_data)
    do_action_depend_on_chart_type(chart_type, grouped_data, key, **kwargs)

    plt.tight_layout()

    chart = get_graph()
    return chart


def get_key(results_by):

    if results_by == '#1':
        key = 'transaction_id'

    elif results_by == '#2':
        key = 'created'

    return key


def do_action_depend_on_chart_type(chart_type, data, key, **kwargs):

    if chart_type == '#1':
        do_bar_chart_action(data, key, **kwargs)

    elif chart_type == '#2':
        do_pie_chart_action(data, key, **kwargs)

    elif chart_type == '#3':
        do_line_chart_action(data, key, **kwargs)

    else:
        print('Failed to identify chart type...')


def do_bar_chart_action(data, key, **kwargs):
    print('bar chart')
    sns.barplot(x=key, y='total_price', data=data)


def do_pie_chart_action(data, key, **kwargs):
    labels = data[key].values
    plt.pie(data=data, x='total_price', labels=labels)


def do_line_chart_action(data, key, **kwargs):
    plt.plot(data[key], data['total_price'], color='green', marker='o')
    print('line chart')

