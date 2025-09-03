const { Telegraf } = require('telegraf');

// getAvailableGifts must return an array of gift objects (as in the provided JSON example)
const { getAvailableGifts } = require('./getAvailableGifts');

function isUpgradeable(gift) {
  return gift.remaining_count !== undefined && gift.total_count !== undefined;
}

function formatGift(gift) {
  const emoji = gift.sticker?.emoji || '🎁';
  let result = `${emoji} ${gift.star_count}⭐`;
  if (isUpgradeable(gift)) {
    result += ' 可升级';
  }
  return result;
}

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!gifts || gifts.length === 0) {
      return ctx.reply('Нет доступных подарков');
    }
    const text = gifts.map(formatGift).join('\n');
    await ctx.reply(text);
  } catch (err) {
    await ctx.reply('Ошибка при получении списка подарков');
  }
});

bot.launch();

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
