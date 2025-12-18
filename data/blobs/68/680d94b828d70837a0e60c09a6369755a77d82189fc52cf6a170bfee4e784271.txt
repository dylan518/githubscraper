package com.molean.tencent.channelbot.service;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.molean.tencent.channelbot.BotApiAccess;
import com.molean.tencent.channelbot.entity.Channel;
import com.molean.tencent.channelbot.post.CreateChannel;
import com.molean.tencent.channelbot.post.UpdateChannel;
import it.unimi.dsi.fastutil.Pair;

import java.net.URI;
import java.util.ArrayList;

public class ChannelService {
    private BotApiAccess botApiAccess;

    private Gson gson;

    public ChannelService(BotApiAccess botApiAccess, Gson gson) {
        this.botApiAccess = botApiAccess;
        this.gson = gson;
    }

    public ArrayList<Channel> getGuildChannels(String guildId) {
        JsonElement jsonElement = botApiAccess.request("GET /guilds/{guild}/channels", Pair.of("guild", guildId));
        ArrayList<Channel> channels = new ArrayList<>();
        for (JsonElement element : jsonElement.getAsJsonArray()) {
            Channel channel = gson.fromJson(element, Channel.class);
            channels.add(channel);
        }
        return channels;
    }

    public Channel getChannelById(String channelId) {
        JsonElement jsonElement = botApiAccess.request("GET /channels/{channel}", Pair.of("channel", channelId));
        return gson.fromJson(jsonElement, Channel.class);
    }

    /*
        name	string	子频道名称
        type	int	子频道类型 ChannelType
        sub_type	int	子频道子类型 ChannelSubType
        position	int	子频道排序，必填；当子频道类型为 子频道分组（ChannelType=4）时，必须大于等于 2
        parent_id	string	子频道所属分组ID
        private_type	int	子频道私密类型 PrivateType
        private_user_ids	string 数组	子频道私密类型成员 ID
        speak_permission	int	子频道发言权限 SpeakPermission
        application_id	string	应用类型子频道应用 AppID，仅应用子频道需要该字段
     */


    public Channel createChannel(String guildId, CreateChannel createChannel) {
        Pair<String, URI> api = botApiAccess.resolveURI("POST /guilds/{guild}/channels", Pair.of("guild", guildId));
        JsonElement jsonElement = botApiAccess.request(api, createChannel);
        return gson.fromJson(jsonElement, Channel.class);
    }

    public Channel updateChannel(String guildId, UpdateChannel updateChannel) {
        Pair<String, URI> api = botApiAccess.resolveURI("PATCH /channels/{guild}", Pair.of("guild", guildId));
        JsonElement jsonElement = botApiAccess.request(api, updateChannel);
        return gson.fromJson(jsonElement, Channel.class);
    }

    public void deleteChannel(String channelId) {
        botApiAccess.request("DELETE /channels/%s".formatted(channelId));
    }

}
