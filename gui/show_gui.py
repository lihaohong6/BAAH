from .components.run_baah_in_gui import run_baah_task
from .pages.Setting_BAAH import set_BAAH
from .pages.Setting_Craft import set_craft
from .pages.Setting_cafe import set_cafe
from .pages.Setting_emulator import set_emulator
from .pages.Setting_event import set_event
from .pages.Setting_exchange import set_exchange
from .pages.Setting_hard import set_hard
from .pages.Setting_normal import set_normal
from .pages.Setting_other import set_other
from .pages.Setting_server import set_server
from .pages.Setting_shop import set_shop
from .pages.Setting_special import set_special
from .pages.Setting_task_order import set_task_order
from .pages.Setting_timetable import set_timetable
from .pages.Setting_wanted import set_wanted
from .pages.Setting_notification import set_notification
from .pages.Setting_vpn import set_vpn
from .pages.Setting_Assault import set_assault
from .pages.Setting_BuyAP import set_buyAP
from .pages.Setting_UserTask import set_usertask
from .define import *

from modules.configs.MyConfig import MyConfigger

import os
from nicegui import ui, run


def show_gui(load_json_name: str):
    """
    the func redner the gui
    Args:
        load_json_name: the json file name in BAAH_CONFIGS
    Returns:
        no return
    """

    config = MyConfigger()

    # wish users do not use example.json, so use bigger and red font to remind users
    if load_json_name == "example.json":
        ui.label(config.get_text("notice_example_json")).style("font-size: 30px; color: red;")

    config.parse_user_config(load_json_name)
    task_name_map = get_task_name_map_dict(config)

    with ui.row().style('min-width: 800px; display: flex; flex-direction: row;flex-wrap: nowrap;'):
        with ui.column().style(
                'height:80vh;min-width: 200px; width: 10vw; overflow: auto;flex-grow: 1; position: sticky; top: 0px;'):
            with ui.card().style('overflow: auto;'):
                ui.link("BAAH", '#BAAH')
                ui.link(config.get_text("setting_emulator"), '#EMULATOR')
                ui.link(config.get_text("setting_server"), '#SERVER')
                ui.link(config.get_text("setting_vpn"), '#VPN')
                ui.link(config.get_text("setting_task_order"), '#TASK_ORDER')
                ui.link(config.get_text("setting_notification"), '#NOTIFICATION')
                # ui.link(config.get_text("setting_next_config"), '#NEXT_CONFIG')
                ui.link(config.get_text("task_cafe"), '#CAFE')
                ui.link(config.get_text("task_timetable"), '#TIME_TABLE')
                ui.link(config.get_text("task_craft"), '#CRAFT')
                ui.link(config.get_text("task_shop"), '#SHOP_NORMAL')
                ui.link(config.get_text("task_buy_ap"), '#BUY_AP')
                ui.link(config.get_text("task_wanted"), '#WANTED')
                ui.link(config.get_text("task_special"), '#SPECIAL_TASK')
                ui.link(config.get_text("task_exchange"), '#EXCHANGE')
                ui.link(config.get_text("task_event"), '#ACTIVITY')
                ui.link(config.get_text("task_assault"), '#ASSAULT')
                ui.link(config.get_text("task_hard"), '#HARD')
                ui.link(config.get_text("task_normal"), '#NORMAL')
                ui.link(config.get_text("task_user_def_task"), '#USER_DEF_TASK')
                ui.link(config.get_text("setting_other"), '#TOOL_PATH')

        with ui.column().style('flex-grow: 4; width: 50vw;'):
            set_BAAH(config, gui_shared_config)

            # 模拟器配置
            set_emulator(config)

            # 服务器配置
            set_server(config)

            # 自己的加速器配置
            set_vpn(config)

            # 任务执行顺序，后续配置文件
            set_task_order(config, task_name_map)

            # 通知
            set_notification(config, gui_shared_config)

            # 咖啡馆
            set_cafe(config)

            # 课程表
            set_timetable(config)

            # 制造
            set_craft(config)

            # 商店
            set_shop(config)

            # 购买AP
            set_buyAP(config)

            # 悬赏通缉
            set_wanted(config)

            # 特殊任务
            set_special(config)

            # 学园交流会
            set_exchange(config)

            # 活动关卡
            set_event(config)

            # 总力战
            set_assault(config)

            # 困难关卡
            set_hard(config, gui_shared_config)

            # 普通关卡
            set_normal(config)

            # 用户定义任务
            set_usertask(config)

            # 其他设置
            set_other(config, load_json_name)

        msg_obj = {
            "stop_signal": 0,
            "runing_signal": 0
        }

        # GUI运行BAAH打印日志的区域
        with ui.column().style('flex-grow: 1;width: 30vw;position:sticky; top: 0px;'):
            output_card = ui.card().style('width: 30vw; height: 80vh;overflow-y: auto;')
            with output_card:
                logArea = ui.log(max_lines=1000).classes('w-full h-full')

        with ui.column().style(
                'width: 10vw; overflow: auto; position: fixed; bottom: 40px; right: 20px;min-width: 150px;'):
            def save_and_alert():
                config.save_user_config(load_json_name)
                config.save_software_config()
                gui_shared_config.save_software_config()
                ui.notify(config.get_text("notice_save_success"))

            ui.button(config.get_text("button_save"), on_click=save_and_alert)

            def save_and_alert_and_run_in_terminal():
                config.save_user_config(load_json_name)
                config.save_software_config()
                gui_shared_config.save_software_config()
                ui.notify(config.get_text("notice_save_success"))
                ui.notify(config.get_text("notice_start_run"))
                # 打开同目录中的BAAH.exe，传入当前config的json文件名
                os.system(f'start BAAH.exe "{load_json_name}"')

            ui.button(config.get_text("button_save_and_run_terminal"), on_click=save_and_alert_and_run_in_terminal)

            # ======Run in GUI======
            async def save_and_alert_and_run():
                config.save_user_config(load_json_name)
                config.save_software_config()
                gui_shared_config.save_software_config()
                ui.notify(config.get_text("notice_save_success"))
                ui.notify(config.get_text("notice_start_run"))
                # 打开同目录中的BAAH.exe，传入当前config的json文件名
                # os.system(f'start BAAH.exe "{load_jsonname}"')
                msg_obj["runing_signal"] = 1
                await run.io_bound(run_baah_task, msg_obj, logArea, config)

            ui.button(config.get_text("button_save_and_run_gui"), on_click=save_and_alert_and_run).bind_visibility_from(
                msg_obj, "runing_signal", backward=lambda x: x == 0)

            async def stop_run() -> None:
                msg_obj["stop_signal"] = 1

            ui.button(config.get_text("notice_finish_run"), on_click=stop_run, color='red').bind_visibility_from(
                msg_obj, "runing_signal", backward=lambda x: x == 1)

            ui.button("...").bind_visibility_from(msg_obj, "runing_signal", backward=lambda x: x == 0.25)

            # ================

    # 加载完毕保存一下config，应用最新的对config的更改
    config.save_user_config(load_json_name)
    config.save_software_config()
