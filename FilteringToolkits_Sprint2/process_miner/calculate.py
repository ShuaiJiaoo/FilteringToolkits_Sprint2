# coding:utf-8

from process_miner.weight import *

# ------- 过滤器 -------
from pm4py.algo.filtering.log.timestamp import timestamp_filter     # 从时间范围过滤，入参为 log
from pm4py.algo.filtering.log.cases import case_filter              # 从时间间隔过滤，入参为 log
from pm4py.algo.filtering.log.attributes import attributes_filter   # 从属性角度过滤，入参为 log
from pm4py.algo.filtering.log.start_activities import start_activities_filter  # 启动活动，入参为 log
from pm4py.algo.filtering.log.end_activities import end_activities_filter      # 最终活动，入参为 log
from pm4py.algo.filtering.pandas.timestamp import timestamp_filter    # 从时间范围过滤，入参为 data_stream
from pm4py.algo.filtering.pandas.cases import case_filter             # 从时间间隔过滤，入参为 data_stream
from pm4py.algo.filtering.pandas.attributes import attributes_filter  # 从属性角度过滤，入参为 data_stream
from pm4py.algo.filtering.pandas.start_activities import start_activities_filter  # 启动活动，入参为 data_stream
from pm4py.algo.filtering.pandas.end_activities import end_activities_filter      # 最终活动，入参为 data_stream


class Filter:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.score = 0
        self.best = 0
        self.weight = None

    @staticmethod
    def sort_filter(filter_list):
        return

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def give_out_best_filter(self):
        return


class Evaluation:
    def __init__(self):
        self.name = ""
        # self.weight = WeightSetting.get_weight("time") 

   
    def assessment(self):
        return

    def get_time_cost(self):
        return

    def get_storage_cost(self):
        return

    def get_accuracy(self):
        return


class Calculate:
    def __init__(self):
        self.mean = 0
        self.median = 0
        self.variance = 0
        self.semi_variance = 0
        self.expected_value = 0
        self.evaluation = Evaluation()

  
    def calculate_accuracy(self, m, md, v, sv, ev):
        return

    
    def get_time_cost(self):
        return self.evaluation.get_time_cost()

    def get_storage_cost(self):
        return self.evaluation.get_storage_cost()

    def get_accuracy(self):
        return self.evaluation.get_accuracy()

    def get_score(self):
        return
