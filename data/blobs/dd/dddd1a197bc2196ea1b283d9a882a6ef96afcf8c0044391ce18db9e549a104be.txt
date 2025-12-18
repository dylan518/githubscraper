package cn.knightzz.design.watcher.chapter02;

import cn.knightzz.design.watcher.chapter02.entity.LotteryResult;
import cn.knightzz.design.watcher.chapter02.event.EventManager;
import cn.knightzz.design.watcher.chapter02.event.annotation.EventType;
import cn.knightzz.design.watcher.chapter02.event.listener.MQEventListener;
import cn.knightzz.design.watcher.chapter02.event.listener.MessageEventListener;

/**
 * @author 王天赐
 * @title: LotteryService
 * @description:
 * @create: 2023-10-11 21:37
 */
public abstract class LotteryService {

    private EventManager eventManager;

    public LotteryService() {

        // 初始化事件管理器
        eventManager = new EventManager(EventType.MQ, EventType.Message);

        // 订阅事件
        eventManager.subscribe(EventType.MQ, new MQEventListener());
        eventManager.subscribe(EventType.Message, new MessageEventListener());
    }

    public LotteryResult draw(String uid) {
        // 执行抽奖
        LotteryResult lotteryResult = doDraw(uid);

        // 执行通知事件
        eventManager.notify(EventType.Message, lotteryResult);
        eventManager.notify(EventType.MQ, lotteryResult);
        return lotteryResult;
    }


    /**
     * 由子类实现的具体抽象方法
     * @param uid 用户的uid
     * @return 抽奖结果
     */
    protected abstract LotteryResult doDraw(String uid) ;
}
