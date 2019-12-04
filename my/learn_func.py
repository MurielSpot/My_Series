#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tmp1():
    from pathlib import Path
    
    print("遍历子目录或者文件:",list(Path("./").iterdir()))
    
    path=Path("./")
    print("判断是否是目录:",Path.is_dir(path))
    
    path=Path("./myBert.py")
    print("判断是否是目录:",Path.is_dir(path))
    
    print("过滤目录(返回生成器):",list(Path("./").glob("*.py")))
    
    print("创建目录:",Path("tmp").mkdir(exist_ok=True))
    
    print("带后缀的完整文件名",Path("./__pycache__/").name)

def tmp2():
    '''
    logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；相比print，具备如下优点：
    可以通过设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息；
    print将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging则可以由开发者决定将信息输出到什么地方，以及怎么输出；
    '''
    import logging
    # logging中可以选择很多消息级别，如debug、info、warning、error以及critical。默认为logging.WARNNING.
    # level = logging.DEBUG
    logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    print(__name__)
    logger = logging.getLogger(__name__)
    print(logger)
    
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

def tmp3():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    # 将日志写入到文件.
    # 设置logging，创建一个FileHandler，并对输出消息的格式进行设置，
    # 将其添加到logger，然后将日志写入到指定的文件中.
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # 将日志同时输出到屏幕和日志文件
    # logger中添加StreamHandler，可以将日志输出到屏幕上，
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

def tmp4():
    from pathlib import Path
    with Path("./myVector.py").open("r",encoding="utf-8") as f:
        print(f.read())
    pass

if __name__=="__main__":
    tmp4()
    pass