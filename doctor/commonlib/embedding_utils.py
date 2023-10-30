import requests
import numpy as np

question = '单位活期存款的利率'
ans0 = '单位大额存单利率与付息方式\n大额存单发行利率分固定利率和浮动利率两种方式。大额存单自认购之日起计息，付息方式分为到期一次还本付息和定期付息。'
ans1 = '单位人民币活期存款介绍\n单位活期存款是指存款单位随时可以存取，不规定存款期限，并依照活期存款利率按季计取利息的存款。'
ans2 = '个人通知存款计息规则\n●个人通知存款在开户时不约定存期，存单上不注明存期和利率。根据存款人通知情况，银行按支取日挂牌公告的相应利率水平和实际存期计息，利随本清。'
token_internal_513 = '人' * 510  # 报错
token_internal_512 = '人' * 509  # 最大token 512
ttoken_stable_513 = '人' * 513  # 报错
ttoken_stable_512 = '人' * 512  # 最大token 512
gt_internal_V100 = [0.680057, 0.766092, 0.597532]
gt_internal_T4 = [0.68005, 0.766097, 0.597484]
gt_stable_V100 = [0.769962, 0.828679, 0.708012]
gt_stable_T4 = [0.769986, 0.82861, 0.708006]

TEST_GROUP = {
    "internal": [
        {
            "input": [question, ans0, ans1, ans2],
            "result": {
                "nova_stage": gt_internal_T4,
                "nova_test": gt_internal_T4,
                "nova_online": gt_internal_V100,
            }
        },
    ],
    "stable": [
        {
            "input": [question, ans0, ans1, ans2],
            "result": {
                "nova_stage": gt_stable_T4,
                "nova_test": gt_stable_T4,
                "nova_online": gt_stable_V100,

            }
        },
    ]

}

INVILD_GROUP = {
    "internal": [
        {
            "input": [question for x in range(33)],
        },
        {
            "input": [token_internal_513, token_internal_512, token_internal_513, token_internal_512],
        },
        {
            "input": [token_internal_512 for x in range(32)],
        },
        {
            "input": [token_internal_512],
        },
    ],
    "stable": [
        {
            "input": [question for x in range(33)],
        },
        {
            "input": [ttoken_stable_513, ttoken_stable_512, ttoken_stable_513, ttoken_stable_512],
            # "input": [ttoken_stable_512],
        },
        {
            "input": [ttoken_stable_512 for x in range(32)],
        },
        {
            "input": [ttoken_stable_512],
        },
    ],

}


def request_s2p(input_list):
    url_s2p = 'http://10.198.6.169:7388/embedding/predict_s2p'
    response = requests.post(url_s2p, json=input_list)
    if response.status_code == 200:
        return response.json()['response']
    else:
        print('请求失败:', response.json())
        raise


def calResult(resp_list):
    res = np.array(resp_list)
    q1, a1, a2, a3 = res[0], res[1], res[2], res[3]
    # 计算向量的模
    norm_q1 = np.linalg.norm(q1)
    norm_a1 = np.linalg.norm(a1)
    norm_a2 = np.linalg.norm(a2)
    norm_a3 = np.linalg.norm(a3)

    # 计算余弦相似度
    similarity_a1 = np.dot(q1, a1) / (norm_q1 * norm_a1)
    similarity_a2 = np.dot(q1, a2) / (norm_q1 * norm_a2)
    similarity_a3 = np.dot(q1, a3) / (norm_q1 * norm_a3)

    print(f"余弦相似度(q1, a1): {round(similarity_a1, 6)}")  # 0.73724
    print(f"余弦相似度(q1, a2): {round(similarity_a2, 6)}")  # 0.73709
    print(f"余弦相似度(q1, a3): {round(similarity_a3, 6)}")  # 0.66003

    # np.save('res.npy', res)
    return round(similarity_a1, 6), round(similarity_a2, 6), round(similarity_a3, 6)


if __name__ == '__main__':
    i_list = [question, ans0, ans1, ans2]
    calResult(request_s2p(i_list))
